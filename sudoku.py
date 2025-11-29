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

    def get_size(self) -> int:
        return self.n * self.n

    def get_num_qubits(self) -> int:
        return self.get_size() + 2 * self.n + 1

def sudoku_line_checker_circuit(grid: SquareGridIndices) -> None:
    for row_idx, row in enumerate(grid.rows()):
        for qubit in row:
            qml.CNOT(wires = [qubit, grid.get_size() + grid.n + row_idx])

    for col_idx, col in enumerate(grid.cols()):
        for qubit in col:
            qml.CNOT(wires = [qubit, grid.get_size() + col_idx])

def sudoku_full_circuit(grid: SquareGridIndices) -> None:
    sudoku_line_checker_circuit(grid)
    qml.MultiControlledX(
        wires = range(grid.get_size(), grid.get_num_qubits()),
        control_values = [True] * (2 * grid.n)
    )
    sudoku_line_checker_circuit(grid)

def grover_diffusion(grid: SquareGridIndices) -> None:
    for i in range(grid.get_size()):
        qml.Hadamard(wires = i)
        qml.PauliX(wires = i)

    # Controlled Z gate
    qml.Hadamard(wires = grid.get_size() - 1)
    qml.MultiControlledX(
        wires = range(grid.get_size()),
        control_values = [True] * (grid.get_size() - 1)
    )
    qml.Hadamard(wires = grid.get_size() - 1)

    for i in range(grid.get_size()):
        qml.PauliX(wires = i)
        qml.Hadamard(wires = i)

if __name__ == "__main__":
    n = 2
    grid = SquareGridIndices(n)
    dev = qml.device("default.qubit", wires = grid.get_num_qubits())

    @qml.qnode(dev)
    def run_qnode():

        for i in range(grid.get_size()):
            qml.Hadamard(wires = i)

        qml.PauliX(wires = grid.get_num_qubits() - 1)
        qml.Hadamard(wires = grid.get_num_qubits() - 1)

        sudoku_full_circuit(grid)
        grover_diffusion(grid)
        sudoku_full_circuit(grid)
        grover_diffusion(grid)

        return qml.probs(wires = range(grid.get_size()))

    probs = run_qnode()
    x = np.arange(len(probs))
    width = 0.5

    fig, ax = plt.subplots(layout='constrained')

    rects = ax.bar(x, probs, width)
    ax.bar_label(rects, padding=3)
    ax.set_ylabel('Probabilité')
    ax.set_title(f"Probabilité de chaque état (sudoku {grid.n}x{grid.n})")

    x_labels = [np.binary_repr(i, width=grid.get_size()) for i in x]

    ax.set_xticks(x, x_labels)

    plt.show()
