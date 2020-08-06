from numpy import zeros
from typing import Tuple
from src.generators.utils import (
    Difficult,
    empty_cells_by_difficult,
    get_random_indices,
)
from src.objects import Sudoku
from src.solvers import naive_solver, recursive_solver
from src.static.constants import EMPTY, SIDE_SIZE, SUDOKU_NUMBERS, SUDOKU_SIZE


def generate(difficult: str = Difficult.easy) -> Tuple[Sudoku, Sudoku]:
    """
    Generates random sudoku using recursion.

    First, algorithm is placing numbers from 1 to 9 in random places into empty sudoku array.
    Secondly, array is filled up to last cell (fully solved sudoku is achieved)
    And, finally, number by number is taken from array till it results in sudoku with only one
    answer.
    """
    # generating empty sudoku
    sudoku = Sudoku(zeros(SUDOKU_SIZE))

    # filling empty sudoku with 9 numbers
    random_indices = get_random_indices(sudoku.where_is_empty, SIDE_SIZE)
    sudoku[random_indices] = SUDOKU_NUMBERS

    # finding solution
    filled_sudoku = recursive_solver(sudoku)
    solved_sudoku = filled_sudoku.copy()

    # emptying sudoku till it have only onve conclusive solution
    while True:
        if naive_solver(solved_sudoku.copy()).is_solved:
            random_indices = get_random_indices(solved_sudoku.where_is_filled)
            last_step_sudoku = solved_sudoku.copy()
            solved_sudoku[random_indices] = EMPTY
        else:
            break

    # refinining the sudoku by its difficult
    random_indices = get_random_indices(
        matrix=last_step_sudoku.where_is_filled, sample_size=empty_cells_by_difficult[difficult],
    )
    last_step_sudoku[random_indices] = EMPTY

    return last_step_sudoku, filled_sudoku
