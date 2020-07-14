import numpy as np

from src.objects import Sudoku
from src.objects.result import Result


def naive_solver(array: np.ndarray) -> np.ndarray:
    sudoku = Sudoku(array)

    while not sudoku.is_solved:
        candidates = sudoku.find_sole_candidates()

        if candidates.size == 0:
            return Result(sudoku, solved=False)

        sudoku.add_numbers(*candidates)

    return Result(sudoku, solved=True)
