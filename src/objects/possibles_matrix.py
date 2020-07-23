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


class PossiblesMatrix:
    __slots__ = ["matrix"]

    def __init__(self):
        self.matrix = generate_empty_possibles_matrix()

    def __setitem__(self, indices, values):
        self.matrix[indices] = values

    def __getitem__(self, indices):
        return self.matrix[indices]

    def __getnotemptyitems__(self, indices):
        return filter_zeros_from_vector(self.matrix[indices])

    def __setsqrs__(self, rows, columns, numbers, values):
        for row, col, number in zip(rows, columns, numbers):
            self.matrix[SQUARE_MAPPING[row], SQUARE_MAPPING[col], number] = EMPTY

    def get_most_promising_cell(self) -> np.ndarray:
        return find_the_least_occuring_element_in_matrix(self.matrix)

    def update_possibilities(self):
        self.set_possibles(ALL, self.filled_columns, self.filled_numbers, EMPTY)
        self.set_possibles(self.filled_rows, ALL, self.filled_numbers, EMPTY)
        self.set_possibles(self.filled_rows, self.filled_columns, ALL, EMPTY)
        self.set_possibles_sqrs(self.filled_rows, self.filled_columns, self.filled_numbers, EMPTY)

    def find_sole_candidates(self) -> np.ndarray:
        self.update_possibilities()
        sole_candidates_rows = find_unique_number(self.matrix, Axis.row)
        sole_candidates_cols = find_unique_number(self.matrix, Axis.column)
        sole_candidates_nbrs = find_unique_number(self.matrix, Axis.number)

        return np.hstack([sole_candidates_rows, sole_candidates_cols, sole_candidates_nbrs])

