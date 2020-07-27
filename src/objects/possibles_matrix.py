import numpy as np

from src.objects.utils import (
    generate_empty_possibles_matrix,
    filter_zeros_from_vector,
    Axis,
    find_unique_number,
)
from src.static.constants import EMPTY, SQUARE_MAPPING,NUMBERS_TYPE, ALL, EMPTY


class PossiblesMatrix:
    __slots__ = ["matrix"]

    def __init__(self):
        self.matrix = generate_empty_possibles_matrix()

    def __setitem__(self, indices, values):
        self.matrix[indices] = values

    def __getitem__(self, indices):
        return self.matrix[indices]

    def __setsqrs__(self, rows, columns, numbers, values):
        for row, col, number in zip(rows, columns, numbers):
            self.matrix[SQUARE_MAPPING[row], SQUARE_MAPPING[col], number] = values

    def __repr__(self):
        return self.matrix.__repr__()

    def get_not_empty_items(self, row, col):
        return filter_zeros_from_vector(self.matrix[row, col])

    def update(self, rows, cols, numbers) -> None:
        self[ALL, cols, numbers] = EMPTY
        self[rows, ALL, numbers] = EMPTY
        self[rows, cols, ALL] = EMPTY
        self.__setsqrs__(rows, cols, numbers, EMPTY)

    def find_sole_candidates(self) -> np.ndarray:
        sole_candidates_rows = find_unique_number(self.matrix, Axis.row)
        sole_candidates_cols = find_unique_number(self.matrix, Axis.column)
        sole_candidates_nbrs = find_unique_number(self.matrix, Axis.number)

        return np.hstack([sole_candidates_rows, sole_candidates_cols, sole_candidates_nbrs])
