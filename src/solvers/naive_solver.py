import numpy as np

from src.objects import Sudoku
from src.objects.result import Result


def naive_solver(array: np.ndarray) -> np.ndarray:
    sudoku = Sudoku(array)

    while not sudoku.is_solved:
        candidates_rows, candidates_cols, candidates_nbrs = sudoku.find_sole_candidates()

        if candidates_rows.size == 0 and candidates_cols.size == 0 and candidates_nbrs.size == 0:
            return Result(sudoku, solved=False)

        sudoku[candidates_rows, candidates_cols] = candidates_nbrs

    return Result(sudoku, solved=True)
