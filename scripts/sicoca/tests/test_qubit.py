"""Tests for SICOCA qubit helpers."""

from __future__ import annotations

import math

import numpy as np

from sicoca import KET_0, KET_1, basis_state, tensor_product, measure, probabilities


class TestQubitHelpers:

    def test_basis_state_zero(self):
        state = basis_state(2, 0)
        expected = np.array([1, 0, 0, 0], dtype=complex)
        np.testing.assert_array_equal(state, expected)

    def test_basis_state_three(self):
        state = basis_state(2, 3)
        expected = np.array([0, 0, 0, 1], dtype=complex)
        np.testing.assert_array_equal(state, expected)

    def test_basis_state_out_of_range(self):
        import pytest
        with pytest.raises(ValueError):
            basis_state(2, 4)

    def test_tensor_product(self):
        result = tensor_product([KET_0, KET_1])
        expected = np.array([0, 1, 0, 0], dtype=complex)
        np.testing.assert_array_almost_equal(result, expected)

    def test_probabilities_sum_to_one(self):
        state = np.array([1 / math.sqrt(2), 1 / math.sqrt(2)], dtype=complex)
        probs = probabilities(state)
        assert abs(probs.sum() - 1.0) < 1e-10

    def test_measure_returns_valid_bitstrings(self):
        state = basis_state(2, 0)
        counts = measure(state, shots=100, seed=0)
        assert list(counts.keys()) == ["00"]

    def test_measure_deterministic_for_basis(self):
        state = basis_state(3, 5)
        counts = measure(state, shots=100, seed=0)
        assert "101" in counts
        assert counts["101"] == 100
