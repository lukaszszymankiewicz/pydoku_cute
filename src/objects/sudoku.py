from typing import Tuple

from copy import deepcopy
from numpy import argwhere, sum
from src.static.types import Vector, Matrix, Index
from src.objects.utils import (
    Axis,
    find_least_filled_place_in_matrix,
    get_matrix_combinations,
    sudoku_is_valid,
)
from src.static.constants import ALL, EMPTY, NUMBERS_TYPE

from .possibles_matrix import PossiblesMatrix


class Sudoku:
    """
    Representation of Sudoku Puzzle.

    Every sudoku is 9x9 cells frame, with every cell filled with number from 1 to 9. Purpose of
    Sudoku puzzle is to filled such that no number repeats in every row, column and 3x3 square.

    This object represents 9x9 array.

    """

    __slots__ = ["array", "_possibles"]

    def __init__(self, array: Matrix):
        self.array = array.astype(NUMBERS_TYPE)
        self._possibles = PossiblesMatrix()

    def __setitem__(self, indices: Vector, values: Vector) -> None:
        self.array[indices] = values

    def __getitem__(self, indices: Matrix) -> Matrix:
        return self.array[indices]

    @property
    def where_is_empty(self) -> Matrix:
        return argwhere(self.array == EMPTY)

    @property
    def where_is_filled(self) -> Matrix:
        return argwhere(self.array != EMPTY)

    @property
    def is_solved(self) -> bool:
        return not EMPTY in self.array

    @property
    def is_solvable(self) -> bool:
        return sum(self._possibles.matrix) != 0

    @property
    def is_valid(self) -> bool:
        return sudoku_is_valid(self.array)

    @property
    def filled_rows(self) -> Matrix:
        return self.where_is_filled[:, Axis.row]

    @property
    def filled_columns(self) -> Matrix:
        return self.where_is_filled[:, Axis.column]

    @property
    def filled_numbers(self) -> Vector:
        return self.array[self.filled_rows, self.filled_columns] - 1

    def copy(self):
        return Sudoku(array=deepcopy(self.array))

    def get_most_promising_cell(self) -> Tuple[Index, Index]:
        return find_least_filled_place_in_matrix(self._possibles.matrix)

    def get_possible_numbers(self, row: Index, col: Index) -> Vector:
        return self._possibles.get_not_empty_items(row, col)

    def get_sudoku_combinations(self, row: Index, column: Index, values: Vector):
        combinations = get_matrix_combinations(self.array, row, column, values)
        return [Sudoku(combination) for combination in combinations]

    def update(self) -> None:
        self._possibles.update(self.filled_rows, self.filled_columns, self.filled_numbers)

    def find_sole_candidates(self) -> Matrix:
        self.update()
        return self._possibles.find_sole_candidates()
