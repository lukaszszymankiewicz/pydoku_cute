import numpy as np

from .nonzero_numbers import NonzeroNumbers
from .possbiles_matrix import PossiblesMatrix


class Sudoku:
    def __init__(self, array: np.array = None, size: int = (9, 9)):
        if array is None:
            self.array = self.generate_empty_sudoku(size)
        else:
            self.array = array
        self.possibles = PossiblesMatrix(self.array)

    @property
    def is_not_solved(self) -> bool:
        return 0 in self.array

    @property
    def nonzero_numbers_indices(self):
        return np.nonzero(self.array)

    @property
    def nonzero_numbers(self):
        return self.array[self.nonzero_numbers_indices] - 1

    def add_numbers(self, numbers: np.array):
        self.array |= numbers

    def generate_empty_sudoku(self, size: tuple) -> np.ndarray:
        return np.zeros(shape=size, dtype=np.uint8)
