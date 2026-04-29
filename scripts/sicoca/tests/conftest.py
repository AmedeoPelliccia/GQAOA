"""Shared pytest fixtures for the SICOCA test suite."""

import pytest

from sicoca import Simulator


@pytest.fixture
def sim():
    """Deterministic simulator fixture with 2048 shots and seed 42."""
    return Simulator(shots=2048, seed=42)
