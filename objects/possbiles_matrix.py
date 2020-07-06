import numpy as np

from .static.square_indices import square_indices, squares
from .utils.generation import generate_empty_possibles_matrix


class PossiblesMatrix:
    __slots__ = ["array"] 

    def __init__(self):
        self.array = generate_empty_possibles_matrix()

    def cross_out_all_numbers_from_position(self, nonzeros):
        self.array[nonzeros.rows, nonzeros.columns, :] = 0

    def cross_out_numbers_from_columns(self, nonzeros):
        self.array[nonzeros.rows, :, nonzeros.numbers] = 0

    def cross_out_numbers_from_rows(self, nonzeros):
        self.array[:, nonzeros.columns, nonzeros.numbers] = 0

    def cross_out_numbers_from_squares(self, nonzeros):
        for row, col, number in zip(nonzeros.rows, nonzeros.columns, nonzeros.numbers):
            self.array[square_indices[row], square_indices[col], number] = 0

    def find_sole_candidate(self, axis:int) -> np.ndarray:
        mask = (self.array != 0).sum(axis=axis, keepdims=True) > 1
        return np.where(mask, 0, self.array).sum(axis=2).astype(np.uint8)

    def xxx(self, array, axis:int) -> np.ndarray:
        mask = (array != 0).sum(axis=axis, keepdims=True) > 1
        return np.where(mask, 0, array).sum(axis=2).astype(np.uint8)

    def find_sole_candidates_in_squares(self) -> np.ndarray:
        empty = np.zeros((9,9)).astype(np.uint8)

        for square in squares:
            to_fill = self.xxx(array=self.array[square[0], square[1]], axis=1)
            empty[square[0], square[1]] == to_fill

        return empty
