import numpy as np

from .nonzero_numbers import NonzeroNumbers
from .possbiles_matrix import PossiblesMatrix
from .utils.generation import generate_empty_sudoku


class Sudoku:
    __slots__ = ["array", "nonzeros", "possibles"]

    def __init__(self, sudoku_to_solve: np.array = None):
        if sudoku_to_solve is None:
            self.array = generate_empty_sudoku((9,9))
        else:
            self.array = sudoku_to_solve

        self.possibles = PossiblesMatrix()
        self.update_nonzeros()

    @property
    def is_not_solved(self) -> bool:
        return 0 in self.array
    
    def update_nonzeros(self):
        self.nonzeros = NonzeroNumbers(self.array)

    def add_numbers(self, numbers: np.array):
        self.array |= numbers

    def add_number(self, row:int, col:int, number:int):
        self.array[row, col] = number

    def update_possibilities(self):
        self.update_nonzeros()

        self.possibles.cross_out_numbers_from_squares(self.nonzeros)
        self.possibles.cross_out_numbers_from_columns(self.nonzeros)
        self.possibles.cross_out_numbers_from_rows(self.nonzeros)
        self.possibles.cross_out_all_numbers_from_position(self.nonzeros)
