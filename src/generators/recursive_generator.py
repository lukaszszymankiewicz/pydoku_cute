import numpy as np

from src.generators.utils import get_random_indices
from src.objects.sudoku import Sudoku
from src.solvers.naive_solver import naive_solver
from src.solvers.recursive_solver import recursive_solver
from src.static.constants import EMPTY, SIDE_SIZE, SUDOKU_NUMBERS, SUDOKU_SIZE


def recursive_conclusive_generator():
    """
    Generates random sudoku using recursion.

    First, algorithm is placing numbers from 1 to 9 in random places into empty sudoku array.
    Secondly, array is filled up to last cell (fully solved sudoku is achieved)
    And, finally, number by number is taken from array till it results in sudoku with only one
    answer.
    """
    sudoku = Sudoku(np.zeros(SUDOKU_SIZE))

    random_indices = get_random_indices(sudoku.where_is_empty, SIDE_SIZE)
    sudoku[random_indices] = SUDOKU_NUMBERS
    solved_sudoku = recursive_solver(sudoku)

    while True:
        if naive_solver(solved_sudoku.copy()).is_solved == True:
            random_indices = get_random_indices(solved_sudoku.where_is_filled)
            last_step_sudoku = solved_sudoku.copy()
            solved_sudoku[random_indices] = EMPTY
        else:
            return last_step_sudoku
