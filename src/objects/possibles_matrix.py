from numpy import hstack
from src.static.types import Vector, Matrix, Scalar
from src.objects.utils import (
    Axis,
    filter_zeros_from_vector,
    find_unique_number,
    generate_empty_possibles_matrix,
)
from src.static.constants import ALL, EMPTY, SQUARE_MAPPING


class PossiblesMatrix:
    __slots__ = ["matrix"]

    def __init__(self) -> None:
        self.matrix = generate_empty_possibles_matrix()

    def __setitem__(self, indices: Matrix, values: Vector) -> None:
        self.matrix[indices] = values

    def __getitem__(self, indices: Matrix) -> Vector:
        return self.matrix[indices]

    def __setsqrs__(self, rows: Vector, columns: Vector, numbers: Vector, values: Vector) -> None:
        for row, col, number in zip(rows, columns, numbers):
            self.matrix[SQUARE_MAPPING[row], SQUARE_MAPPING[col], number] = values

    def get_not_empty_items(self, row: Scalar, col: Scalar) -> Vector:
        return filter_zeros_from_vector(self.matrix[row, col])

    def update(self, rows:Vector, cols: Vector, numbers: Vector) -> None:
        self[ALL, cols, numbers] = EMPTY
        self[rows, ALL, numbers] = EMPTY
        self[rows, cols, ALL] = EMPTY
        self.__setsqrs__(rows, cols, numbers, EMPTY)

    def find_sole_candidates(self) -> Matrix:
        sole_candidates_rows = find_unique_number(self.matrix, Axis.row)
        sole_candidates_cols = find_unique_number(self.matrix, Axis.column)
        sole_candidates_nbrs = find_unique_number(self.matrix, Axis.number)

        return hstack([sole_candidates_rows, sole_candidates_cols, sole_candidates_nbrs])
