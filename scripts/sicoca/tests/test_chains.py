"""Tests for SICOCA interlocking chains, predicates, and chain manager."""

from __future__ import annotations

import pytest

from sicoca import (
    Circuit, Simulator, SimulationResult,
    Chain, ChainManager, Link, LinkStatus,
    always_proceed, majority_outcome, fidelity_threshold,
    basis_state, bell_pair,
)
from sicoca.tests import make_dummy_result


# =========================================================================
# Interlock predicates
# =========================================================================

class TestInterlockPredicates:

    def test_always_proceed(self):
        r = make_dummy_result({"00": 100})
        assert always_proceed(r) is True

    def test_majority_outcome_pass(self):
        pred = majority_outcome("00")
        assert pred(make_dummy_result({"00": 90, "11": 10})) is True

    def test_majority_outcome_fail(self):
        pred = majority_outcome("00")
        assert pred(make_dummy_result({"11": 90, "00": 10})) is False

    def test_majority_outcome_empty_counts(self):
        pred = majority_outcome("00")
        # majority_outcome should treat empty counts as a failing interlock
        assert pred(make_dummy_result({})) is False

    def test_fidelity_threshold_pass(self):
        ref = basis_state(2, 0)
        pred = fidelity_threshold(0.99, ref)
        r = SimulationResult("t", 2, basis_state(2, 0))
        assert pred(r) is True

    def test_fidelity_threshold_fail(self):
        ref = basis_state(2, 0)
        pred = fidelity_threshold(0.99, ref)
        r = SimulationResult("t", 2, basis_state(2, 3))
        assert pred(r) is False


# =========================================================================
# Chain
# =========================================================================

class TestChain:

    def test_chain_add_link(self):
        chain = Chain(name="test")
        chain.add_link(Circuit(2).h(0))
        assert len(chain.links) == 1

    def test_chain_fluent(self):
        chain = Chain(name="test")
        chain.add_link(Circuit(2).h(0)).add_link(Circuit(2).x(0))
        assert len(chain.links) == 2


# =========================================================================
# Chain manager
# =========================================================================

class TestChainManager:

    def test_register_and_execute(self, sim):
        mgr = ChainManager(simulator=sim)
        chain = Chain(name="simple")
        chain.add_link(bell_pair(), label="Bell")
        mgr.register_chain(chain)
        results = mgr.execute_chain("simple")
        assert len(results) == 1
        assert isinstance(results[0], SimulationResult)

    def test_duplicate_registration_raises(self, sim):
        mgr = ChainManager(simulator=sim)
        mgr.register_chain(Chain(name="dup"))
        with pytest.raises(ValueError):
            mgr.register_chain(Chain(name="dup"))

    def test_execute_unknown_raises(self, sim):
        mgr = ChainManager(simulator=sim)
        with pytest.raises(KeyError):
            mgr.execute_chain("nonexistent")

    def test_chain_blocks_on_interlock(self, sim):
        mgr = ChainManager(simulator=sim)
        chain = Chain(name="blocking")
        chain.add_link(bell_pair(), label="Bell")
        chain.add_link(Circuit(2).x(0),
                       interlock=lambda _result: False,
                       label="Should block")
        mgr.register_chain(chain)
        mgr.execute_chain("blocking")
        link1 = chain.links[1]
        assert link1.status is LinkStatus.BLOCKED

    def test_chain_proceeds_with_always(self, sim):
        mgr = ChainManager(simulator=sim)
        chain = Chain(name="proceed")
        chain.add_link(Circuit(1).h(0), label="H")
        chain.add_link(Circuit(1).x(0), interlock=always_proceed, label="X")
        mgr.register_chain(chain)
        results = mgr.execute_chain("proceed")
        assert len(results) == 2

    def test_execute_all(self, sim):
        mgr = ChainManager(simulator=sim)
        mgr.register_chain(Chain(name="a").add_link(Circuit(1).h(0)))
        mgr.register_chain(Chain(name="b").add_link(Circuit(1).x(0)))
        all_results = mgr.execute_all()
        assert set(all_results.keys()) == {"a", "b"}

    def test_summary_string(self, sim):
        mgr = ChainManager(simulator=sim)
        chain = Chain(name="sum")
        chain.add_link(Circuit(1).h(0))
        mgr.register_chain(chain)
        mgr.execute_chain("sum")
        summary = mgr.summary()
        assert "SICOCA" in summary
        assert "sum" in summary


# =========================================================================
# LinkStatus enum coverage
# =========================================================================

class TestLinkStatus:
    """Verify all expected LinkStatus enum values exist."""

    def test_pending_exists(self):
        assert LinkStatus.PENDING is not None

    def test_passed_exists(self):
        assert LinkStatus.PASSED is not None

    def test_blocked_exists(self):
        assert LinkStatus.BLOCKED is not None

    def test_executed_exists(self):
        assert LinkStatus.EXECUTED is not None

    def test_all_values(self):
        names = {s.name for s in LinkStatus}
        assert names == {"PENDING", "PASSED", "BLOCKED", "EXECUTED"}
