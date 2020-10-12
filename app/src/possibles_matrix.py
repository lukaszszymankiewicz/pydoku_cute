import numpy as np

from .constants import ALL, EMPTY, SQUARE_MAPPING
from .types import Matrix, Scalar, Vector
from .utils import (
    Axis,
    filter_zeros_from_vector,
    find_unique_number,
    generate_empty_possibles_matrix,
)


class PossiblesMatrix:
    """
    Holds possible numbers to be filled in every cell of Sudoku.

    Cause sudoku is 9x9 cells array, and every cell can have every number from 1 to 9, empty
    possibles matrix is basically 9x9x9 numpy array cube.

    Placing new number in sudoku array updates its possibles matrix (cause every new numbers
    "blocks" other number in its row, cols and square).
    """

    __slots__ = ["matrix"]

    def __init__(self) -> None:
        self.matrix = generate_empty_possibles_matrix()

    def __setitem__(self, indices: Matrix, values: Vector) -> None:
        self.matrix[indices] = values

    def __getitem__(self, indices: Matrix) -> Vector:
        return self.matrix[indices]

    def __setsqrs__(self, rows: Vector, columns: Vector, numbers: Vector, values: Vector) -> None:
        """Sets values in 3x3 squares.
        
        Values to be places are chosen using three vectors: representation of rows, cols and
        numbers.

        Attrs:
            rows: flat numpy vector represents rows position of numbers to be filled, 
            cols: flat numpy vector represents cols position of numbers to be filled, 
            numbers: flat numpy vector represents numbers to be filled,
            values: flat numpy vector of number to be filled in inputted place.
        """
        for row, col, number in zip(rows, columns, numbers):
            self.matrix[SQUARE_MAPPING[row], SQUARE_MAPPING[col], number] = values

    def get_not_empty_items(self, row: Scalar, col: Scalar) -> Vector:
        return filter_zeros_from_vector(self.matrix[row, col])

    def update(self, rows: Vector, cols: Vector, numbers: Vector) -> None:
        """Updates PossiblesMatrix after placing new number in sudoku.

        New numbers are represented by three flat numpy vectors: its coordinates in rows and cols, 
        and its numbers.

        Attrs:
            rows: flat numpy vector represents rows position of numbers to be filled, 
            cols: flat numpy vector represents cols position of numbers to be filled, 
            numbers: flat numpy vector represents numbers to be filled.

        Returns:
            None.
        """
        self[ALL, cols, numbers] = EMPTY
        self[rows, ALL, numbers] = EMPTY
        self[rows, cols, ALL] = EMPTY
        self.__setsqrs__(rows, cols, numbers, EMPTY)

    def find_sole_candidates(self) -> Matrix:
        """Searches PossiblesMatrix for numbers which is sole candidate to be put into sudoku.

        Attrs:
            None.

        Returns:
            2d numpy array representing sole candidates to be put into sudoku puzzle.
        """
        sole_candidates_rows = find_unique_number(self.matrix, Axis.row)
        sole_candidates_cols = find_unique_number(self.matrix, Axis.column)
        sole_candidates_nbrs = find_unique_number(self.matrix, Axis.number)

        return np.hstack([sole_candidates_rows, sole_candidates_cols, sole_candidates_nbrs])
