import numpy as np
import random
from .naive_solver import naive_solver


def recursive_solver(sudoku):
    sudokus = [sudoku]

    while True:
        result = naive_solver(sudokus.pop())

        if result.is_solved == False:
            if result.is_solvable:
                cell_row, cell_col = result.get_most_promising_cell()
                possible_number = result.get_possible_numbers(cell_row, cell_col)
                new_sudokus = result.get_sudoku_combinations(cell_row, cell_col, possible_number)
                sudokus.extend(new_sudokus)
            else:
                continue
        else:
            if sudoku_is_valid3(result.array):
                return result
            else:
                random.shuffle(sudokus)


def sudoku_is_valid3(array: np.ndarray) -> bool:
    for row in array:
        if len(set(row)) != len(row):
            return False

    return True
def sudoku_is_valid2(array: np.ndarray) -> bool:
    for row in array:
        if np.any(np.bincount(row) > 1):
            return False

    return True
