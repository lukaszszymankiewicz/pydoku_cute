import numpy as np

from src.objects.utils import (
    Axis,
    generate_empty_possibles_matrix,
    find_the_least_occuring_element_in_matrix,
    get_matrix_combinations,
    find_unique_number,
    filter_zeros_from_vector,
)
from src.static.constants import NUMBERS_TYPE, ALL, EMPTY, SQUARE_MAPPING
from copy import deepcopy


class Sudoku:
    __slots__ = ["array", "_possibles"]

    def __init__(self, array: np.array):
        self.array = array.astype(NUMBERS_TYPE)
        self._possibles_matrix = generate_empty_possibles_matrix()

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

    def copy(self):
        return Sudoku(array=deepcopy(self.array))

    def get_possibles(self, rows, columns):
        return self._possibles[rows, columns]

    def get_possibles_numbers(self, rows, columns):
        return filter_zeros_from_vector(self.get_possibles(rows, columns))

    def set_possibles(self, rows, columns, numbers, values):
        self._possibles[rows, columns, numbers] = values

    def set_possibles_sqrs(self, rows, columns, numbers, values):
        for row, col, number in zip(rows, columns, numbers):
            self._possibles[SQUARE_MAPPING[row], SQUARE_MAPPING[col], number] = EMPTY

    def get_most_promising_cell(self) -> np.ndarray:
        return find_the_least_occuring_element_in_matrix(self._possibles)

    def get_sudoku_combinations(self, row, column, values):
        combinations = get_matrix_combinations(self.array, row, column, values)
        return [Sudoku(combination) for combination in combinations]

    def update_possibilities(self):
        self.set_possibles(ALL, self.filled_columns, self.filled_numbers, EMPTY)
        self.set_possibles(self.filled_rows, ALL, self.filled_numbers, EMPTY)
        self.set_possibles(self.filled_rows, self.filled_columns, ALL, EMPTY)
        self.set_possibles_sqrs(self.filled_rows, self.filled_columns, self.filled_numbers, EMPTY)

    def find_sole_candidates(self) -> np.ndarray:
        self.update_possibilities()
        sole_candidates_rows = find_unique_number(self._possibles, Axis.row)
        sole_candidates_cols = find_unique_number(self._possibles, Axis.column)
        sole_candidates_nbrs = find_unique_number(self._possibles, Axis.number)

        return np.hstack([sole_candidates_rows, sole_candidates_cols, sole_candidates_nbrs])
