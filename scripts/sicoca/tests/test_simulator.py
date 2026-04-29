"""Tests for SICOCA statevector simulator."""

from __future__ import annotations

import math

import numpy as np

from sicoca import (
    Circuit, Simulator, SimulationResult,
    KET_0, KET_1, X, basis_state, bell_pair, ghz_state,
)


class TestSimulator:

    def test_identity_circuit(self, sim):
        c = Circuit(1, name="identity")
        result = sim.run(c)
        np.testing.assert_array_almost_equal(result.statevector, KET_0)

    def test_x_gate(self, sim):
        c = Circuit(1, name="x").x(0)
        result = sim.run(c)
        np.testing.assert_array_almost_equal(result.statevector, KET_1)

    def test_h_creates_superposition(self, sim):
        c = Circuit(1, name="h").h(0)
        result = sim.run(c)
        expected = np.array([1 / math.sqrt(2), 1 / math.sqrt(2)], dtype=complex)
        np.testing.assert_array_almost_equal(result.statevector, expected)

    def test_bell_state(self, sim):
        c = bell_pair()
        result = sim.run(c, shots=4096)
        sv = result.statevector
        expected = np.array([1 / math.sqrt(2), 0, 0, 1 / math.sqrt(2)],
                            dtype=complex)
        np.testing.assert_array_almost_equal(sv, expected)
        assert set(result.counts.keys()).issubset({"00", "11"})

    def test_cnot_no_flip_when_control_zero(self, sim):
        c = Circuit(2).cnot(0, 1)
        result = sim.run(c)
        np.testing.assert_array_almost_equal(
            result.statevector, basis_state(2, 0)
        )

    def test_cnot_flips_when_control_one(self, sim):
        c = Circuit(2).x(0).cnot(0, 1)
        result = sim.run(c)
        np.testing.assert_array_almost_equal(
            result.statevector, basis_state(2, 3)
        )

    def test_non_adjacent_cnot(self, sim):
        c = Circuit(3).x(0).cnot(0, 2)
        result = sim.run(c)
        np.testing.assert_array_almost_equal(
            result.statevector, basis_state(3, 5)
        )

    def test_reversed_cnot(self, sim):
        c = Circuit(2).x(1).cnot(1, 0)
        result = sim.run(c)
        np.testing.assert_array_almost_equal(
            result.statevector, basis_state(2, 3)
        )

    def test_ghz_state_superposition(self, sim):
        c = ghz_state(3)
        result = sim.run(c)
        expected = np.zeros(8, dtype=complex)
        expected[0] = 1 / math.sqrt(2)
        expected[7] = 1 / math.sqrt(2)
        np.testing.assert_array_almost_equal(result.statevector, expected)

    def test_double_x_is_identity(self, sim):
        c = Circuit(1).x(0).x(0)
        result = sim.run(c)
        np.testing.assert_array_almost_equal(result.statevector, KET_0)

    def test_hzh_equals_x(self, sim):
        c = Circuit(1).h(0).z(0).h(0)
        result = sim.run(c)
        expected = X.matrix @ KET_0
        np.testing.assert_array_almost_equal(result.statevector, expected)

    def test_custom_initial_state(self, sim):
        c = Circuit(1, name="noop")
        result = sim.run(c, initial_state=KET_1)
        np.testing.assert_array_almost_equal(result.statevector, KET_1)

    # -- Additional coverage: Y-gate simulation --------------------------------

    def test_y_gate(self, sim):
        """Y|0⟩ = i|1⟩"""
        c = Circuit(1, name="y").y(0)
        result = sim.run(c)
        expected = np.array([0, 1j], dtype=complex)
        np.testing.assert_array_almost_equal(result.statevector, expected)

    # -- Additional coverage: SimulationResult repr/fields ---------------------

    def test_simulation_result_repr(self, sim):
        c = Circuit(1, name="repr_test").x(0)
        result = sim.run(c)
        r = repr(result)
        assert "repr_test" in r
        assert "n_qubits=1" in r

    def test_simulation_result_fields(self, sim):
        c = Circuit(1, name="fields_test").h(0)
        result = sim.run(c)
        assert result.circuit_name == "fields_test"
        assert result.n_qubits == 1
        assert result.statevector is not None
        probs = result.probabilities
        assert abs(probs.sum() - 1.0) < 1e-10

    def test_simulation_result_empty_counts_repr(self):
        """SimulationResult with empty counts should still have a valid repr."""
        result = SimulationResult(
            circuit_name="empty", n_qubits=1,
            statevector=basis_state(1, 0),
        )
        r = repr(result)
        assert "empty" in r
