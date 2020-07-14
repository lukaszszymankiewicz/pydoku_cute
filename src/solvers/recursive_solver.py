import numpy as np

from .naive_solver import naive_solver

from src.objects import Sudoku
from src.objects.result import Result


def recursive_solver(array: np.ndarray):
    sudokus = [array]
    nodes = 0
    branches = 0

    while True:
        result = naive_solver(sudokus.pop(-1))

        if not result.is_solved:
            inconclusive_sudoku = result.sudoku
            indices = inconclusive_sudoku.get_most_promising_cell()
            possible_numbers = inconclusive_sudoku.get_possible_values(indices)
            sudokus.extend(inconclusive_sudoku.get_sudoku_combinations(indices, possible_numbers))

            nodes += 1
            branches += len(possible_numbers)

        else:
            result.solved=True,
            result.nodes = nodes
            result.branches = branches
            return result
