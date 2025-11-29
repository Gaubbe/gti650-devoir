import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

# Typing
import pennylane.typing as qmlt
from typing import Iterable

class SquareGridIndices:
    def __init__(self, n: int) -> None:
        self.n = n

    def row(self, row_num: int) -> Iterable[int]:
        assert row_num < self.n and row_num >= 0, "row_num must be a positive number lower than n"
        return range(row_num * self.n, (row_num + 1) * self.n)

    def col(self, col_num: int) -> Iterable[int]:
        assert col_num < self.n and col_num >= 0, "col_num must be a positive number lower than n"
        return range(col_num, self.n * self.n, self.n)

    def rows(self) -> Iterable[Iterable[int]]:
        return map(lambda idx: self.row(idx), range(self.n))

    def cols(self) -> Iterable[Iterable[int]]:
        return map(lambda idx: self.col(idx), range(self.n))

    def get_num_qubits(self) -> int:
        return self.n * self.n + 2 * self.n + 1

def sudoku_line_checker_circuit(grid: SquareGridIndices) -> None:
    for row_idx, row in enumerate(grid.rows()):
        for qubit in row:
            qml.CNOT(wires = [qubit, grid.n * grid.n + grid.n + row_idx])

    for col_idx, col in enumerate(grid.cols()):
        for qubit in col:
            qml.CNOT(wires = [qubit, grid.n * grid.n + col_idx])

def sudoku_full_circuit(grid: SquareGridIndices) -> None:
    sudoku_line_checker_circuit(grid)
    qml.MultiControlledX(
        wires = range(grid.n * grid.n, grid.get_num_qubits()),
        control_values = [True] * (2 * grid.n)
    )
    sudoku_line_checker_circuit(grid)

if __name__ == "__main__":
    n = 3
    num_qubits = n * n + 2 * n + 1
    dev = qml.device("default.qubit", wires = num_qubits)
    grid = SquareGridIndices(n)

    inputs = [np.binary_repr(i, width=n * n) for i in range(2**(n * n))]

    @qml.qnode(dev)
    def run_qnode(input: str):
        for qubit, initial_value in enumerate(reversed(input)):
            if initial_value == "1":
                qml.PauliX(wires = qubit)

        sudoku_full_circuit(grid)

        return qml.probs()

    for input in inputs:
        probs = run_qnode(input)
        result = np.argmax(probs)
        if result & 0b1 == 1:
            print(np.binary_repr(result, width = num_qubits))

