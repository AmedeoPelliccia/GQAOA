"""Tests for SICOCA circuit builder and templates."""

from __future__ import annotations

import pytest

from sicoca import Circuit, bell_pair, ghz_state, superdense_coding_encode


class TestCircuit:

    def test_add_gate_h(self):
        c = Circuit(2)
        c.h(0)
        assert c.depth == 1

    def test_fluent_api(self):
        c = Circuit(2).h(0).cnot(0, 1)
        assert c.depth == 2

    def test_qubit_index_out_of_range(self):
        c = Circuit(2)
        with pytest.raises(IndexError):
            c.h(2)

    def test_bell_pair_template(self):
        c = bell_pair()
        assert c.depth == 2
        assert c.n_qubits == 2

    def test_ghz_state_template(self):
        c = ghz_state(4)
        assert c.depth == 4  # H + 3 CNOTs
        assert c.n_qubits == 4

    def test_ghz_minimum(self):
        with pytest.raises(ValueError):
            ghz_state(1)

    def test_circuit_copy_is_independent(self):
        c = Circuit(2).h(0)
        c2 = c.copy()
        c2.x(1)
        assert c.depth == 1
        assert c2.depth == 2

    def test_draw_returns_string(self):
        c = bell_pair()
        diagram = c.draw()
        assert "q0:" in diagram
        assert "q1:" in diagram

    # -- Additional coverage: draw edge cases ---------------------------------

    def test_draw_zero_gate_circuit(self):
        """A circuit with no gates should still produce valid wire labels."""
        c = Circuit(2)
        diagram = c.draw()
        assert "q0:" in diagram
        assert "q1:" in diagram

    def test_draw_large_circuit(self):
        """Drawing a circuit with many gates should not error."""
        c = Circuit(3)
        for _ in range(20):
            c.h(0).x(1).z(2)
        diagram = c.draw()
        assert "q0:" in diagram
        assert "q2:" in diagram

    # -- Additional coverage: superdense coding encode -------------------------

    def test_superdense_coding_encode_00(self):
        """Encoding (0, 0) should produce an empty circuit (no gates)."""
        c = superdense_coding_encode(0, 0)
        assert c.depth == 0

    def test_superdense_coding_encode_01(self):
        """Encoding (0, 1) should apply X only."""
        c = superdense_coding_encode(0, 1)
        assert c.depth == 1
        assert c.operations[0].name == "X"

    def test_superdense_coding_encode_10(self):
        """Encoding (1, 0) should apply Z only."""
        c = superdense_coding_encode(1, 0)
        assert c.depth == 1
        assert c.operations[0].name == "Z"

    def test_superdense_coding_encode_11(self):
        """Encoding (1, 1) should apply X then Z."""
        c = superdense_coding_encode(1, 1)
        assert c.depth == 2
        assert c.operations[0].name == "X"
        assert c.operations[1].name == "Z"

    # -- Additional coverage: Y gate on circuit --------------------------------

    def test_y_gate_on_circuit(self):
        """Circuit.y() should add a Y gate."""
        c = Circuit(1).y(0)
        assert c.depth == 1
        assert c.operations[0].name == "Y"
