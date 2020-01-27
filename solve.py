import numpy as np

from pydoku.enum import Axis
from pydoku.objects import NonzeroNumbers, PossiblesMatrix, Sudoku


def solve(array: np.ndarray):
    possibles = PossiblesMatrix(array)
    sudoku = Sudoku(array)

    while sudoku.is_not_solved:
        nonzeros = NonzeroNumbers(sudoku)

        possibles.cross_out_all_numbers_from_position(nonzeros)
        possibles.cross_out_numbers_from_columns(nonzeros)
        possibles.cross_out_numbers_from_rows(nonzeros)
        possibles.cross_out_numbers_from_squares(nonzeros)

        sudoku.add_numbers(possibles.lonely_numbers(Axis.number))
        sudoku.add_numbers(possibles.lonely_numbers(Axis.row))
        sudoku.add_numbers(possibles.lonely_numbers(Axis.column))

    return sudoku.array
