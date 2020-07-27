import numpy as np

from .naive_solver import naive_solver


def recursive_solver(sudoku):
    sudokus = [sudoku]

    while True:
        sudoku = naive_solver(sudokus.pop(-1))

        if not sudoku.is_solved:
            cell_row, cell_col = sudoku.get_most_promising_cell()
            possible_number = sudoku.get_possible_numbers(cell_row, cell_col)
            new_sudokus = sudoku.get_sudoku_combinations(cell_row, cell_col, possible_number)
            sudokus.extend(new_sudokus)

        else:
            return sudoku
