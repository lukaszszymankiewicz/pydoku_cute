import numpy as np

from .naive_solver import naive_solver

from src.objects.result import Result


def recursive_solver(array: np.ndarray):
    sudokus = [array]
    nodes = 0
    branches = 0

    while True:
        result = naive_solver(sudokus.pop(-1))

        if not result.is_solved:
            inconclusive_sudoku = result.sudoku
            cell_row, cell_col = inconclusive_sudoku.get_most_promising_cell()
            numbers = inconclusive_sudoku.get_possibles_numbers(cell_row, cell_col)
            new_sudokus = inconclusive_sudoku.get_sudoku_combinations(cell_row, cell_col, numbers)
            sudokus.extend(new_sudokus)

            nodes += 1
            branches += len(numbers)

        else:
            result.solved = True
            result.nodes = nodes
            result.branches = branches
            return result
