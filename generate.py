import numpy as np

from pydoku.objects import NonzeroNumbers, PossiblesMatrix, Sudoku


def generate(digits_num: int = 20, size: int = 9):
    sudoku_array = np.zeros((size, size), dtype=np.int)
    sudoku = Sudoku(sudoku_array)
    possibles = PossiblesMatrix(sudoku_array)

    while np.count_nonzero(sudoku.array) < digits_num:
        nonzeros = np.nonzero(possibles.array)
        idx = np.random.randint(0, nonzeros[0].size)

        row = nonzeros[0][idx]
        col = nonzeros[1][idx]
        nbr = nonzeros[2][idx]

        sudoku.array[row, col] = nbr + 1
        breakpoint()
        nonzeros = NonzeroNumbers(sudoku)

        possibles.cross_out_all_numbers_from_position(nonzeros)
        possibles.cross_out_numbers_from_columns(nonzeros)
        possibles.cross_out_numbers_from_rows(nonzeros)
        possibles.cross_out_numbers_from_squares(nonzeros)

    return sudoku.array

