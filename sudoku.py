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

if __name__ == "__main__":
    grid = SquareGridIndices(3)

    for i in range(grid.n):
        row_idx = list(grid.row(i))
        print(f"row_idx[{i}] = {row_idx}")

        col_idx = list(grid.col(i))
        print(f"col_idx[{i}] = {col_idx}")
