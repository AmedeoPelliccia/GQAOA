"""Tests for SICOCA gate definitions and binding."""

from __future__ import annotations

import numpy as np

from sicoca import Gate, H, X, Y, Z, I, CNOT, get_gate, GATE_CATALOGUE, KET_0, KET_1


# =========================================================================
# Gate matrix properties
# =========================================================================

class TestGateDefinitions:
    """Verify matrix properties of all gates."""

    def test_hadamard_is_unitary(self):
        product = H.matrix @ H.matrix.conj().T
        np.testing.assert_array_almost_equal(product, np.eye(2))

    def test_hadamard_is_hermitian(self):
        np.testing.assert_array_almost_equal(H.matrix, H.matrix.conj().T)

    def test_pauli_x_squares_to_identity(self):
        np.testing.assert_array_almost_equal(X.matrix @ X.matrix, np.eye(2))

    def test_pauli_y_squares_to_identity(self):
        np.testing.assert_array_almost_equal(Y.matrix @ Y.matrix, np.eye(2))

    def test_pauli_z_squares_to_identity(self):
        np.testing.assert_array_almost_equal(Z.matrix @ Z.matrix, np.eye(2))

    def test_pauli_x_flips_zero(self):
        result = X.matrix @ KET_0
        np.testing.assert_array_almost_equal(result, KET_1)

    def test_pauli_x_flips_one(self):
        result = X.matrix @ KET_1
        np.testing.assert_array_almost_equal(result, KET_0)

    def test_pauli_z_phase_flips(self):
        result = Z.matrix @ KET_1
        np.testing.assert_array_almost_equal(result, -KET_1)

    def test_cnot_matrix_shape(self):
        assert CNOT.matrix.shape == (4, 4)

    def test_cnot_is_unitary(self):
        product = CNOT.matrix @ CNOT.matrix.conj().T
        np.testing.assert_array_almost_equal(product, np.eye(4))

    def test_gate_catalogue_contains_all(self):
        for name in ("H", "X", "Y", "Z", "I", "CNOT", "CX"):
            assert name in GATE_CATALOGUE

    def test_get_gate_lookup(self):
        assert get_gate("H") is H
        assert get_gate("cnot") is CNOT

    def test_get_gate_unknown_raises(self):
        import pytest
        with pytest.raises(KeyError):
            get_gate("TOFFOLI")


# =========================================================================
# Gate binding
# =========================================================================

class TestGateBind:
    """Verify gate binding to qubit indices."""

    def test_bind_single_qubit(self):
        bound = H.bind(2)
        assert bound.target_qubits == (2,)

    def test_bind_two_qubit(self):
        bound = CNOT.bind(0, 3)
        assert bound.target_qubits == (0, 3)

    def test_bind_wrong_count_raises(self):
        import pytest
        with pytest.raises(ValueError):
            H.bind(0, 1)

    def test_bind_negative_raises(self):
        import pytest
        with pytest.raises(ValueError):
            H.bind(-1)

    def test_bind_duplicate_raises(self):
        import pytest
        with pytest.raises(ValueError):
            CNOT.bind(1, 1)
