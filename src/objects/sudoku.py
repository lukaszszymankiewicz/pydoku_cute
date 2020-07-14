import numpy as np

from .nonzero_numbers import NonzeroNumbers

from src.objects.utils import (
    ALL,
    EMPTY,
    SQUARE_INDICES,
    SQUARES,
    Axis,
    generate_empty_possibles_matrix,
    find_the_least_occuring_element_in_matrix,
    create_matrix_combinations_with_one_changed_value,
    find_unique_number,
    filter_zeros_from_vector,
    )


class Sudoku:
    __slots__ = ["array", "_nonzeros", "_possibles"]

    def __init__(self, array: np.array):
        self.array = array
        self._possibles = generate_empty_possibles_matrix()
        self.update_nonzeros()

    @property
    def is_solved(self) -> bool:
        return not EMPTY in self.array

    def update_nonzeros(self):
        self._nonzeros = NonzeroNumbers(self.array)

    def add_numbers(self, rows: np.ndarray, cols: np.ndarray, numbers: np.ndarray):
        # TODO: maybe __setitem__? 
        self.array[rows, cols] = numbers + 1

    def cross_out_numbers_from_possibles(self, axis:int):
        indices = [self._nonzeros.rows, self._nonzeros.columns, self._nonzeros.numbers]
        indices[axis] = ALL
        self._possibles[indices] = EMPTY

    def cross_out_numbers_from_squares(self):
        # TODO: this functions needs to be renamed
        for row, col, number in self._nonzeros:
            self._possibles[SQUARE_INDICES[row], SQUARE_INDICES[col], number] = EMPTY

    def get_most_promising_cell(self) -> np.ndarray:
        return find_the_least_occuring_element_in_matrix(self._possibles)

    def get_possible_values(self, indices) -> np.ndarray:
        return filter_zeros_from_vector(self._possibles[tuple(indices)])
    
    def get_sudoku_combinations(self, indices, values):
        return create_matrix_combinations_with_one_changed_value(self.array, indices, values)

    def update_possibilities(self):
        self.update_nonzeros()

        self.cross_out_numbers_from_possibles(axis=Axis.row)
        self.cross_out_numbers_from_possibles(axis=Axis.column)
        self.cross_out_numbers_from_possibles(axis=Axis.number)
        self.cross_out_numbers_from_squares()

    def find_sole_candidates(self) -> np.ndarray:
        self.update_possibilities()

        sole_candidates_rows = find_unique_number(self._possibles, Axis.row)
        sole_candidates_cols = find_unique_number(self._possibles, Axis.column)
        sole_candidates_nbrs = find_unique_number(self._possibles, Axis.number)
       
        return np.hstack([sole_candidates_rows, sole_candidates_cols, sole_candidates_nbrs])

