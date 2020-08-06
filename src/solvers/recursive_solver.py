from random import shuffle

from src.objects.sudoku import Sudoku

from src.solvers import naive_solver


def recursive_solver(sudoku: Sudoku) -> Sudoku:
    sudokus = [sudoku]

    while True:
        result = naive_solver(sudokus.pop())

        if not result.is_solved:
            if result.is_solvable:
                cell_row, cell_col = result.get_most_promising_cell()
                possible_number = result.get_possible_numbers(cell_row, cell_col)
                new_sudokus = result.get_sudoku_combinations(cell_row, cell_col, possible_number)
                sudokus.extend(new_sudokus)
        else:
            if not result.is_valid:
                shuffle(sudokus)
            else:
                return result
