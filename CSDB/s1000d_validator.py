#!/usr/bin/env python3
"""
S1000D Data Module XSD-Style Validator
=======================================
Validates a descriptive DM against S1000D 5.0 structural rules.

Since the official S1000D XSD schemas are licensed material,
this validator implements the key structural and business-rule
checks that the XSD would enforce, plus additional BREX-level
checks relevant to the AMPEL360 project.

Usage:
    python CSDB/s1000d_validator.py <path-to-dm.xml>
    python CSDB/s1000d_validator.py <directory>       # validate all .xml in tree
    python CSDB/s1000d_validator.py --self-test       # run built-in checks

Exit codes:
    0  – all validations passed
    1  – one or more errors detected
    2  – usage / IO error
"""

from __future__ import annotations

import argparse
import enum
import re
import sys
import textwrap
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence

# ---------------------------------------------------------------------------
# Constants — S1000D 5.0 & AMPEL360 project rules
# ---------------------------------------------------------------------------

#: Regex for a valid S1000D-style Data Module Code used by AMPEL360.
#: Pattern: MODEL-DIFF-SYS-SUBSYS-SUBSUBSYS-ASSY-DISASSY-VARIANT-INFOCODE-ITEMLOC
#: Example: AMPEL360-A-51-00-00-00A-040A-A
DMC_PATTERN = re.compile(
    r"^[A-Z0-9]{2,14}"       # model identifier (e.g. AMPEL360)
    r"-[A-Z]"                 # system difference code
    r"-\d{2}"                 # system code (ATA chapter)
    r"-\d{2}"                 # sub-system
    r"-\d{2}"                 # sub-sub-system
    r"-\d{2}[A-Z0-9]"        # assy/disassy code + variant
    r"-\d{3}[A-Z]"           # information code + item-location-code
    r"-[A-Z]$"               # learn code / variant
)

#: Valid S1000D information code prefixes (first three digits).
#: Subset most relevant to AMPEL360.
VALID_INFO_CODES: set = {
    "000",  # General
    "010",  # Title page
    "018",  # Change record
    "040",  # Description
    "100",  # Removal
    "200",  # Servicing
    "300",  # Examination/Check
    "400",  # Other maintenance
    "500",  # Inspection
    "520",  # Clean/Paint
    "600",  # Repair
    "700",  # Setting/adjusting
    "720",  # Calibration
    "800",  # Test/fault-isolation
    "900",  # Crew operations
    "920",  # Training
    "940",  # Wiring data
    "941",  # Wiring diagram
}

#: ATA chapter range accepted by the project (00–99).
VALID_ATA_RANGE = range(0, 100)

#: Recognised Q-Division identifiers.
Q_DIVISIONS = frozenset({
    "Q-AIR",
    "Q-GREENTECH",
    "Q-STRUCTURES",
    "Q-HPC",
    "Q-DATAGOV",
    "Q-INDUSTRY",
    "Q-SPACE",
    "Q-GROUND",
    "Q-MECHANICS",
    "Q-SCIRES",
})

#: Mapping of ATA chapter → expected Q-Division(s) for BREX validation.
ATA_QDIVISION_MAP: Dict[str, List[str]] = {
    "00": ["Q-DATAGOV"],
    "05": ["Q-DATAGOV"],
    "06": ["Q-INDUSTRY"],
    "10": ["Q-GROUND"],
    "20": ["Q-MECHANICS"],
    "21": ["Q-MECHANICS"],
    "24": ["Q-GREENTECH"],
    "27": ["Q-AIR"],
    "28": ["Q-GREENTECH"],
    "29": ["Q-MECHANICS"],
    "32": ["Q-MECHANICS"],
    "42": ["Q-HPC"],
    "46": ["Q-HPC"],
    "51": ["Q-STRUCTURES"],
    "52": ["Q-STRUCTURES"],
    "53": ["Q-STRUCTURES"],
    "54": ["Q-STRUCTURES"],
    "55": ["Q-STRUCTURES"],
    "56": ["Q-STRUCTURES"],
    "57": ["Q-STRUCTURES"],
    "71": ["Q-GREENTECH"],
    "72": ["Q-GREENTECH"],
    "73": ["Q-GREENTECH"],
    "80": ["Q-SCIRES"],
    "93": ["Q-SPACE"],
}

#: Quantum-signature regex (matches signatures produced by CSDBGenesisManager).
QUANTUM_SIGNATURE_PATTERN = re.compile(
    r"^QS-[A-Z_]+-[a-f0-9]{8}-[01]{4}-\d{14}$"
)

#: Date ISO-8601 format used by AMPEL360.
DATE_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2})?$"
)

#: ICN reference format.
ICN_PATTERN = re.compile(r"^ICN-[A-Z]{3}-\d{4}$")


# ---------------------------------------------------------------------------
# Severity & result model
# ---------------------------------------------------------------------------


class Severity(enum.Enum):
    """Validation finding severity."""

    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class Finding:
    """Single validation finding."""

    rule_id: str
    severity: Severity
    message: str
    location: str
    suggestion: Optional[str] = None

    def __str__(self) -> str:
        parts = [
            f"[{self.severity.value}] {self.rule_id}: {self.message}",
            f"  Location: {self.location}",
        ]
        if self.suggestion:
            parts.append(f"  Suggestion: {self.suggestion}")
        return "\n".join(parts)


@dataclass
class ValidationReport:
    """Aggregated results for one or more data modules."""

    findings: List[Finding] = field(default_factory=list)

    @property
    def errors(self) -> List[Finding]:
        return [f for f in self.findings if f.severity == Severity.ERROR]

    @property
    def warnings(self) -> List[Finding]:
        return [f for f in self.findings if f.severity == Severity.WARNING]

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0

    def summary(self) -> str:
        return (
            f"Findings: {len(self.findings)} total — "
            f"{len(self.errors)} error(s), {len(self.warnings)} warning(s), "
            f"{len(self.findings) - len(self.errors) - len(self.warnings)} info(s). "
            f"Result: {'PASS' if self.passed else 'FAIL'}"
        )


# ---------------------------------------------------------------------------
# Validator engine
# ---------------------------------------------------------------------------


class S1000DValidator:
    """Validates XML data modules against S1000D 5.0 structural rules
    and AMPEL360 BREX business rules.

    The validator does **not** require the licensed S1000D XSD schemas.
    Instead it re-implements the structural constraints programmatically.
    """

    # ---- public API -------------------------------------------------------

    def validate_file(self, path: Path) -> ValidationReport:
        """Validate a single XML data module file."""
        report = ValidationReport()
        loc = str(path)

        if not path.is_file():
            report.findings.append(Finding(
                rule_id="IO-001",
                severity=Severity.ERROR,
                message=f"File not found: {path}",
                location=loc,
            ))
            return report

        # 1. Well-formedness ---------------------------------------------------
        try:
            tree = ET.parse(str(path))
        except ET.ParseError as exc:
            report.findings.append(Finding(
                rule_id="XML-001",
                severity=Severity.ERROR,
                message=f"XML is not well-formed: {exc}",
                location=loc,
                suggestion="Fix XML syntax errors before re-validating.",
            ))
            return report  # can't continue without a parse tree

        root = tree.getroot()

        # 2. Structural checks (XSD-equivalent) --------------------------------
        self._check_root_element(root, loc, report)
        self._check_ident_section(root, loc, report)
        self._check_content_section(root, loc, report)
        self._check_dmc_format(root, loc, report)
        self._check_language(root, loc, report)
        self._check_dm_title(root, loc, report)
        self._check_procedural_structure(root, loc, report)

        # 3. BREX / business-rule checks ----------------------------------------
        self._check_info_code(root, loc, report)
        self._check_ata_chapter(root, loc, report)
        self._check_dates(root, loc, report)
        self._check_quantum_signature(root, loc, report)
        self._check_icn_references(root, loc, report)
        self._check_q_division(root, loc, report)
        self._check_warning_placement(root, loc, report)

        return report

    def validate_directory(self, directory: Path) -> ValidationReport:
        """Recursively validate every ``*.xml`` file under *directory*."""
        report = ValidationReport()
        xml_files = sorted(directory.rglob("*.xml"))
        if not xml_files:
            report.findings.append(Finding(
                rule_id="IO-002",
                severity=Severity.WARNING,
                message=f"No XML files found under {directory}",
                location=str(directory),
            ))
            return report
        for xml_path in xml_files:
            sub = self.validate_file(xml_path)
            report.findings.extend(sub.findings)
        return report

    # ---- structural checks (XSD-equivalent) --------------------------------

    def _check_root_element(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        tag = _local_name(root.tag)
        if tag != "dmodule":
            report.findings.append(Finding(
                rule_id="XSD-001",
                severity=Severity.ERROR,
                message=f"Root element must be <dmodule>, found <{tag}>",
                location=loc,
                suggestion="Wrap content inside a <dmodule> root element.",
            ))

    def _check_ident_section(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        ident = _find(root, "identAndStatusSection")
        if ident is None:
            report.findings.append(Finding(
                rule_id="XSD-002",
                severity=Severity.ERROR,
                message="Missing required <identAndStatusSection>",
                location=loc,
                suggestion=(
                    "Add an <identAndStatusSection> containing "
                    "<dmAddress> with <dmIdent> and <dmAddressItems>."
                ),
            ))
            return

        dm_address = _find(ident, "dmAddress")
        if dm_address is None:
            report.findings.append(Finding(
                rule_id="XSD-003",
                severity=Severity.ERROR,
                message="Missing required <dmAddress> in <identAndStatusSection>",
                location=loc,
            ))
            return

        dm_ident = _find(dm_address, "dmIdent")
        if dm_ident is None:
            report.findings.append(Finding(
                rule_id="XSD-004",
                severity=Severity.ERROR,
                message="Missing required <dmIdent> in <dmAddress>",
                location=loc,
            ))

    def _check_content_section(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        content = _find(root, "content")
        if content is None:
            report.findings.append(Finding(
                rule_id="XSD-005",
                severity=Severity.ERROR,
                message="Missing required <content> section in <dmodule>",
                location=loc,
                suggestion="Add a <content> element containing the DM payload.",
            ))

    def _check_dmc_format(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        for dmc_el in _findall(root, "dmCode"):
            text = (dmc_el.text or "").strip()
            if not text:
                report.findings.append(Finding(
                    rule_id="XSD-006",
                    severity=Severity.ERROR,
                    message="<dmCode> element is empty",
                    location=loc,
                ))
                continue
            if not DMC_PATTERN.match(text):
                report.findings.append(Finding(
                    rule_id="XSD-006",
                    severity=Severity.ERROR,
                    message=f"Invalid DMC format: {text}",
                    location=f"{loc} -> <dmCode>",
                    suggestion=(
                        "Expected pattern: MODEL-DIFF-SYS-SUBSYS-SUBSUBSYS-"
                        "ASSY_DISASSY_VARIANT-INFOCODE_ITEMLOC-LEARNCODE  "
                        "e.g. AMPEL360-A-51-00-00-00A-040A-A"
                    ),
                ))

    def _check_language(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        lang_el = _find_deep(root, "language")
        if lang_el is None:
            return  # optional element
        iso_code = _find(lang_el, "languageIsoCode")
        country = _find(lang_el, "countryIsoCode")
        if iso_code is not None:
            code = (iso_code.text or "").strip().lower()
            if code and len(code) != 2:
                report.findings.append(Finding(
                    rule_id="XSD-007",
                    severity=Severity.WARNING,
                    message=f"languageIsoCode should be ISO 639-1 (2 chars), got '{code}'",
                    location=f"{loc} -> <languageIsoCode>",
                ))
        if country is not None:
            cc = (country.text or "").strip().upper()
            if cc and len(cc) != 2:
                report.findings.append(Finding(
                    rule_id="XSD-008",
                    severity=Severity.WARNING,
                    message=f"countryIsoCode should be ISO 3166-1 alpha-2, got '{cc}'",
                    location=f"{loc} -> <countryIsoCode>",
                ))

    def _check_dm_title(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        title_el = _find_deep(root, "dmTitle")
        if title_el is None:
            report.findings.append(Finding(
                rule_id="XSD-009",
                severity=Severity.WARNING,
                message="Missing <dmTitle> — recommended for every data module",
                location=loc,
            ))
            return
        tech_name = _find(title_el, "techName")
        if tech_name is None or not (tech_name.text or "").strip():
            report.findings.append(Finding(
                rule_id="XSD-010",
                severity=Severity.WARNING,
                message="<dmTitle> present but <techName> is missing or empty",
                location=f"{loc} -> <dmTitle>",
            ))

    def _check_procedural_structure(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        """Validate procedural DMs have required sub-elements."""
        content = _find(root, "content")
        if content is None:
            return
        procedure = _find(content, "procedure")
        if procedure is None:
            return  # not a procedural DM — skip

        # S1000D requires preliminaryRqmts before mainProcedure
        prelim = _find(procedure, "preliminaryRqmts")
        main_proc = _find(procedure, "mainProcedure")

        if main_proc is None:
            report.findings.append(Finding(
                rule_id="XSD-011",
                severity=Severity.ERROR,
                message="<procedure> must contain a <mainProcedure> element",
                location=f"{loc} -> <procedure>",
            ))
        if prelim is None:
            report.findings.append(Finding(
                rule_id="XSD-012",
                severity=Severity.WARNING,
                message="<preliminaryRqmts> is recommended in <procedure>",
                location=f"{loc} -> <procedure>",
            ))

        # Check each proceduralStep has content
        if main_proc is not None:
            for step in _findall(main_proc, "proceduralStep"):
                para = _find(step, "para")
                if para is None or not (para.text or "").strip():
                    step_id = step.get("id", "unknown")
                    report.findings.append(Finding(
                        rule_id="XSD-013",
                        severity=Severity.WARNING,
                        message=f"Procedural step '{step_id}' has no <para> text",
                        location=f"{loc} -> <proceduralStep id='{step_id}'>",
                    ))

    # ---- BREX / business-rule checks ---------------------------------------

    def _check_info_code(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        """BREX: information code portion of DMC must be a recognised code."""
        for dmc_el in _findall(root, "dmCode"):
            text = (dmc_el.text or "").strip()
            if not text:
                continue
            # Extract info-code segment (3 digits after last '-' cluster)
            parts = text.split("-")
            if len(parts) >= 7:
                info_seg = parts[-2]  # e.g. '040A'
                info_code = info_seg[:3] if len(info_seg) >= 3 else info_seg
                if info_code.isdigit() and info_code not in VALID_INFO_CODES:
                    report.findings.append(Finding(
                        rule_id="BREX-001",
                        severity=Severity.WARNING,
                        message=f"Unrecognised information code '{info_code}' in DMC '{text}'",
                        location=f"{loc} -> <dmCode>",
                        suggestion=f"Valid codes include: {', '.join(sorted(VALID_INFO_CODES))}",
                    ))

    def _check_ata_chapter(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        """BREX: ATA chapter (system code) must be 00–99."""
        for dmc_el in _findall(root, "dmCode"):
            text = (dmc_el.text or "").strip()
            if not text:
                continue
            parts = text.split("-")
            if len(parts) >= 3:
                sys_code = parts[2]
                if sys_code.isdigit():
                    chapter = int(sys_code)
                    if chapter not in VALID_ATA_RANGE:
                        report.findings.append(Finding(
                            rule_id="BREX-002",
                            severity=Severity.ERROR,
                            message=f"ATA chapter '{sys_code}' out of range (00-99) in DMC '{text}'",
                            location=f"{loc} -> <dmCode>",
                        ))

    def _check_dates(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        """BREX: dates should use ISO-8601."""
        for tag_name in ("issueDate", "date", "modificationDate"):
            for el in _findall(root, tag_name):
                text = (el.text or "").strip()
                # Also check 'year'/'month'/'day' attribute-style dates
                if not text:
                    year = el.get("year", "")
                    month = el.get("month", "")
                    day = el.get("day", "")
                    if year:
                        text = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                if text and not DATE_PATTERN.match(text):
                    report.findings.append(Finding(
                        rule_id="BREX-003",
                        severity=Severity.WARNING,
                        message=f"Date '{text}' does not match ISO-8601 (YYYY-MM-DD[THH:MM:SS])",
                        location=f"{loc} -> <{tag_name}>",
                    ))

    def _check_quantum_signature(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        """BREX/AMPEL360: quantum signatures must match project format."""
        for el in _findall(root, "quantumSignature"):
            text = (el.text or "").strip()
            if text and not QUANTUM_SIGNATURE_PATTERN.match(text):
                report.findings.append(Finding(
                    rule_id="BREX-004",
                    severity=Severity.ERROR,
                    message=f"Invalid quantum signature format: {text}",
                    location=f"{loc} -> <quantumSignature>",
                    suggestion=(
                        "Expected: QS-<DIVISION>-<8 hex chars>-<4 binary>-<14 digit timestamp>"
                    ),
                ))

    def _check_icn_references(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        """BREX: Information Control Number references must match format."""
        for el in _findall(root, "icnRef"):
            text = (el.text or el.get("infoControlNumberFileRef", "")).strip()
            if text and not ICN_PATTERN.match(text):
                report.findings.append(Finding(
                    rule_id="BREX-005",
                    severity=Severity.WARNING,
                    message=f"Invalid ICN reference format: {text}",
                    location=f"{loc} -> <icnRef>",
                    suggestion="Expected: ICN-XXX-NNNN",
                ))

    def _check_q_division(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        """BREX/AMPEL360: if a Q-Division owner tag exists, validate it."""
        for el in _findall(root, "responsiblePartnerCompany"):
            # Could be in an attribute or child element
            div = (el.text or el.get("enterpriseCode", "")).strip()
            if div and div.startswith("Q-") and div not in Q_DIVISIONS:
                report.findings.append(Finding(
                    rule_id="BREX-006",
                    severity=Severity.WARNING,
                    message=f"Unrecognised Q-Division: {div}",
                    location=f"{loc} -> <responsiblePartnerCompany>",
                    suggestion=f"Valid divisions: {', '.join(sorted(Q_DIVISIONS))}",
                ))

    def _check_warning_placement(
        self, root: ET.Element, loc: str, report: ValidationReport
    ) -> None:
        """BREX: <warning> must appear *before* <para> inside a proceduralStep.

        S1000D mandates that warnings/cautions precede the instructional
        text they relate to.
        """
        for step in _findall(root, "proceduralStep"):
            children = list(step)
            warning_indices = [
                i for i, ch in enumerate(children)
                if _local_name(ch.tag) in ("warning", "caution")
            ]
            para_indices = [
                i for i, ch in enumerate(children)
                if _local_name(ch.tag) == "para"
            ]
            if warning_indices and para_indices:
                first_para = min(para_indices)
                for wi in warning_indices:
                    if wi > first_para:
                        step_id = step.get("id", "unknown")
                        report.findings.append(Finding(
                            rule_id="BREX-007",
                            severity=Severity.WARNING,
                            message=(
                                f"<warning>/<caution> appears after <para> in "
                                f"proceduralStep '{step_id}'; S1000D requires "
                                f"warnings before the procedural text"
                            ),
                            location=f"{loc} -> <proceduralStep id='{step_id}'>",
                            suggestion=(
                                "Move <warning>/<caution> elements before the "
                                "first <para> in each procedural step."
                            ),
                        ))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _local_name(tag: str) -> str:
    """Strip namespace prefix from an element tag."""
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def _find(parent: ET.Element, local: str) -> Optional[ET.Element]:
    """Find first direct child matching *local* (namespace-agnostic)."""
    for child in parent:
        if _local_name(child.tag) == local:
            return child
    return None


def _find_deep(root: ET.Element, local: str) -> Optional[ET.Element]:
    """Depth-first search for the first element matching *local*."""
    for el in root.iter():
        if _local_name(el.tag) == local:
            return el
    return None


def _findall(root: ET.Element, local: str) -> List[ET.Element]:
    """Return all descendant elements matching *local* (namespace-agnostic)."""
    return [el for el in root.iter() if _local_name(el.tag) == local]


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="s1000d_validator",
        description=(
            "Validate S1000D 5.0 data modules against structural (XSD-style) "
            "and BREX business rules for the AMPEL360 project."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            examples:
              %(prog)s DM/PROCEDURAL/PROC-001_Battery_Maintenance_Procedure.xml
              %(prog)s DM/                    # validate all .xml recursively
              %(prog)s --self-test             # run built-in sanity checks
        """),
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Path to an XML data module file or directory.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run built-in self-tests and exit.",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Only print the summary line.",
    )
    return parser


def _run_self_tests() -> bool:
    """Execute built-in validation self-tests.  Returns True on success."""
    validator = S1000DValidator()
    all_ok = True

    def _assert(condition: bool, label: str) -> None:
        nonlocal all_ok
        status = "PASS" if condition else "FAIL"
        if not condition:
            all_ok = False
        print(f"  [{status}] {label}")

    print("Running self-tests …\n")

    # --- Test 1: valid descriptive DM ----------------------------------------
    valid_dm = textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <dmodule xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <identAndStatusSection>
            <dmAddress>
              <dmIdent>
                <dmCode>AMPEL360-A-51-00-00-00A-040A-A</dmCode>
                <language>
                  <languageIsoCode>en</languageIsoCode>
                  <countryIsoCode>US</countryIsoCode>
                </language>
              </dmIdent>
              <dmAddressItems>
                <dmTitle>
                  <techName>BWB Structural Configuration</techName>
                  <infoName>Description</infoName>
                </dmTitle>
              </dmAddressItems>
            </dmAddress>
          </identAndStatusSection>
          <content>
            <description>
              <para>Primary structural layout of the BWB airframe.</para>
            </description>
          </content>
        </dmodule>
    """)
    tmp_valid = Path("/tmp/_s1000d_test_valid.xml")
    tmp_valid.write_text(valid_dm, encoding="utf-8")
    r1 = validator.validate_file(tmp_valid)
    _assert(r1.passed, "Valid descriptive DM produces no errors")
    _assert(len(r1.errors) == 0, f"  error count == 0 (got {len(r1.errors)})")

    # --- Test 2: missing root ------------------------------------------------
    bad_root = '<?xml version="1.0"?>\n<notAModule><foo/></notAModule>'
    tmp_bad = Path("/tmp/_s1000d_test_bad_root.xml")
    tmp_bad.write_text(bad_root, encoding="utf-8")
    r2 = validator.validate_file(tmp_bad)
    _assert(not r2.passed, "Wrong root element triggers error")
    _assert(
        any(f.rule_id == "XSD-001" for f in r2.errors),
        "  error XSD-001 raised",
    )

    # --- Test 3: bad DMC format ----------------------------------------------
    bad_dmc_dm = textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <dmodule>
          <identAndStatusSection>
            <dmAddress>
              <dmIdent>
                <dmCode>BAD-FORMAT-1234</dmCode>
              </dmIdent>
            </dmAddress>
          </identAndStatusSection>
          <content><description><para>x</para></description></content>
        </dmodule>
    """)
    tmp_dmc = Path("/tmp/_s1000d_test_bad_dmc.xml")
    tmp_dmc.write_text(bad_dmc_dm, encoding="utf-8")
    r3 = validator.validate_file(tmp_dmc)
    _assert(
        any(f.rule_id == "XSD-006" for f in r3.errors),
        "Invalid DMC triggers XSD-006",
    )

    # --- Test 4: missing content section -------------------------------------
    no_content = textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <dmodule>
          <identAndStatusSection>
            <dmAddress>
              <dmIdent>
                <dmCode>AMPEL360-A-51-00-00-00A-040A-A</dmCode>
              </dmIdent>
            </dmAddress>
          </identAndStatusSection>
        </dmodule>
    """)
    tmp_nc = Path("/tmp/_s1000d_test_no_content.xml")
    tmp_nc.write_text(no_content, encoding="utf-8")
    r4 = validator.validate_file(tmp_nc)
    _assert(
        any(f.rule_id == "XSD-005" for f in r4.errors),
        "Missing <content> triggers XSD-005",
    )

    # --- Test 5: warning after para (BREX-007) --------------------------------
    bad_order = textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <dmodule>
          <identAndStatusSection>
            <dmAddress><dmIdent>
              <dmCode>AMPEL360-A-71-00-00-00A-040A-A</dmCode>
            </dmIdent></dmAddress>
          </identAndStatusSection>
          <content>
            <procedure>
              <preliminaryRqmts/>
              <mainProcedure>
                <proceduralStep id="step01">
                  <para>Do something.</para>
                  <warning><warningAndCautionPara>Danger!</warningAndCautionPara></warning>
                </proceduralStep>
              </mainProcedure>
            </procedure>
          </content>
        </dmodule>
    """)
    tmp_order = Path("/tmp/_s1000d_test_warning_order.xml")
    tmp_order.write_text(bad_order, encoding="utf-8")
    r5 = validator.validate_file(tmp_order)
    _assert(
        any(f.rule_id == "BREX-007" for f in r5.findings),
        "Warning after <para> triggers BREX-007",
    )

    # --- Test 6: valid procedural DM -----------------------------------------
    valid_proc = textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <dmodule>
          <identAndStatusSection>
            <dmAddress><dmIdent>
              <dmCode>AMPEL360-A-71-00-00-00A-200A-A</dmCode>
            </dmIdent></dmAddress>
          </identAndStatusSection>
          <content>
            <procedure>
              <preliminaryRqmts>
                <reqCondGroup>
                  <noConds>Aircraft power OFF</noConds>
                </reqCondGroup>
              </preliminaryRqmts>
              <mainProcedure>
                <proceduralStep id="s1">
                  <warning><warningAndCautionPara>High voltage!</warningAndCautionPara></warning>
                  <para>Disconnect main bus.</para>
                </proceduralStep>
              </mainProcedure>
            </procedure>
          </content>
        </dmodule>
    """)
    tmp_proc = Path("/tmp/_s1000d_test_valid_proc.xml")
    tmp_proc.write_text(valid_proc, encoding="utf-8")
    r6 = validator.validate_file(tmp_proc)
    _assert(r6.passed, "Valid procedural DM passes without errors")

    # --- Test 7: malformed XML -----------------------------------------------
    tmp_malformed = Path("/tmp/_s1000d_test_malformed.xml")
    tmp_malformed.write_text("<dmodule><broken", encoding="utf-8")
    r7 = validator.validate_file(tmp_malformed)
    _assert(
        any(f.rule_id == "XML-001" for f in r7.errors),
        "Malformed XML triggers XML-001",
    )

    # --- Test 8: DMC pattern matches known good codes -------------------------
    good_codes = [
        "AMPEL360-A-51-00-00-00A-040A-A",
        "AMPEL360-A-27-00-00-00A-040A-A",
        "AMPEL360-A-71-00-00-00A-040A-A",
        "AMPEL360-A-42-00-00-00A-040A-A",
        "AMPEL360-A-00-00-00-00A-040A-A",
    ]
    for code in good_codes:
        _assert(
            DMC_PATTERN.match(code) is not None,
            f"DMC_PATTERN accepts '{code}'",
        )

    # Clean up
    for tmp in (tmp_valid, tmp_bad, tmp_dmc, tmp_nc, tmp_order, tmp_proc, tmp_malformed):
        tmp.unlink(missing_ok=True)

    print(f"\nSelf-test result: {'ALL PASSED' if all_ok else 'SOME FAILED'}")
    return all_ok


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        return 0 if _run_self_tests() else 1

    if args.path is None:
        parser.print_help()
        return 2

    target = Path(args.path)
    validator = S1000DValidator()

    if target.is_dir():
        report = validator.validate_directory(target)
    elif target.is_file():
        report = validator.validate_file(target)
    else:
        print(f"Error: path not found: {target}", file=sys.stderr)
        return 2

    if not args.quiet:
        for finding in report.findings:
            print(finding)
            print()

    print(report.summary())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
