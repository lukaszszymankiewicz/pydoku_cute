from typing import Tuple

import numpy as np

from .constants import EMPTY, SIDE_SIZE, SUDOKU_NUMBERS, SUDOKU_SIZE
from .enums import Difficult, empty_cells_by_difficult
from .naive_solver import naive_solver
from .recursive_solver import recursive_solver
from .sudoku import Sudoku
from .utils import get_random_indices


def generate(difficult: str = Difficult.default) -> Tuple[Sudoku, Sudoku]:
    """
    Generates random sudoku using recursion.

    First, algorithm is placing numbers from 1 to 9 in random places into empty sudoku array.
    Secondly, array is filled up to last cell (fully solved sudoku is achieved)
    And, finally, number by number is taken from array till it results in sudoku with only one
    answer.
    To achieve sudokus with different diffuculties, as a last step some random cells are emptied
    from such generated sudoku.

    Args:
        difficult: difficult of sudoku to be generated.

    Returns:
        Two Sudoku objects: one unsolved, and other which is solution to that one.
    """
    # generating empty sudoku
    sudoku = Sudoku(np.zeros(SUDOKU_SIZE))

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
