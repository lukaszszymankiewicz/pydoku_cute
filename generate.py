import numpy as np

from objects import NonzeroNumbers, PossiblesMatrix, Sudoku
from util import Axis


def generate(n_numbers_to_fill: int = 10):
    sudoku = Sudoku()

    for _ in range(n_numbers_to_fill):
        # Firstly, I`m choosing random square on sudoku array which does not have any number on it.
        a = np.argwhere(sudoku.array==0)
        b = np.random.randint(a.shape[0])
        c = a[b]

        # Seconly, I1`m taking indices of this empty square and check which number are aveilable
        # there.
        number_to_put = np.random.choice(sudoku.possibles.array[c[0], c[1]])
        cc = sudoku.possibles.array[c[0], c[1]]
        b = np.nonzero(cc)

        a = np.random.choice(b[0])
        sudoku.array[c[0], c[1]] = number_to_put

        # Finally this number should be cross out from possibles
        nonzeros = NonzeroNumbers(sudoku)

        sudoku.possibles.cross_out_all_numbers_from_position(nonzeros)
        sudoku.possibles.cross_out_numbers_from_columns(nonzeros)
        sudoku.possibles.cross_out_numbers_from_rows(nonzeros)
        sudoku.possibles.cross_out_numbers_from_squares(nonzeros)

    return sudoku.array

print(generate())

