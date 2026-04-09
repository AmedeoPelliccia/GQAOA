"""
SICOCA test suite
=================
Run all tests::

    python -m pytest scripts/sicoca/tests/ -v
"""

from sicoca import SimulationResult, basis_state


def make_dummy_result(counts=None, n_qubits=2, index=0):
    """Factory for test ``SimulationResult`` instances.

    Parameters
    ----------
    counts : dict or None
        Measurement outcome counts.  Defaults to ``{"00": 100}``.
    n_qubits : int
        Number of qubits for the result.
    index : int
        Basis state index for the statevector.

    Returns
    -------
    SimulationResult
    """
    counts = counts or {"00": 100}
    return SimulationResult(
        circuit_name="test",
        n_qubits=n_qubits,
        statevector=basis_state(n_qubits, index),
        counts=counts,
    )
