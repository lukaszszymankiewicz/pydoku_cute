from copy import deepcopy

import numpy as np

from src.objects.utils import (
    Axis,
    find_least_filled_place_in_matrix,
    find_unique_number,
    get_matrix_combinations,
    sudoku_is_valid,
)
from src.static.constants import ALL, EMPTY, NUMBERS_TYPE

from .possibles_matrix import PossiblesMatrix


class Sudoku:
    __slots__ = ["array", "_possibles"]

    def __init__(self, array: np.array):
        self.array = array.astype(NUMBERS_TYPE)
        self._possibles = PossiblesMatrix()

    def __setitem__(self, indices, values):
        self.array[indices] = values

    def __getitem__(self, indices):
        return self.array[indices]

    def __repr__(self):
        return self.array.__repr__()

    @property
    def where_is_empty(self) -> np.ndarray:
        return np.argwhere(self.array == EMPTY)

    @property
    def where_is_filled(self) -> np.ndarray:
        return np.argwhere(self.array != EMPTY)

    @property
    def is_solved(self) -> bool:
        return not EMPTY in self.array

    @property
    def filled_rows(self):
        return self.where_is_filled[:, Axis.row]

    @property
    def filled_columns(self):
        return self.where_is_filled[:, Axis.column]

    @property
    def filled_numbers(self):
        return self.array[self.filled_rows, self.filled_columns] - 1

    @property
    def is_solvable(self):
        return np.sum(self._possibles.matrix) != 0

    def copy(self):
        return Sudoku(array=deepcopy(self.array))

    def get_most_promising_cell(self) -> np.ndarray:
        return find_least_filled_place_in_matrix(self._possibles.matrix)

    def get_possible_numbers(self, row: int, col: int) -> np.ndarray:
        return self._possibles.get_not_empty_items(row, col)

    def get_sudoku_combinations(self, row: int, column: int, values: np.ndarray):
        combinations = get_matrix_combinations(self.array, row, column, values)
        return [Sudoku(combination) for combination in combinations]

    def update(self) -> None:
        self._possibles.update(self.filled_rows, self.filled_columns, self.filled_numbers)

    def find_sole_candidates(self) -> np.ndarray:
        self.update()
        return self._possibles.find_sole_candidates()
