import numpy as np

from src.objects import Sudoku
from src.objects.utils.enums import Axis
from src.static.samples import sample1


def naive_solver(array: np.ndarray) -> np.ndarray:
    sudoku = Sudoku(array)

    while sudoku.is_not_solved:
        sudoku.update_possibilities()

        sole_candidates_rows = sudoku.possibles.find_sole_candidate(Axis.row)
        sole_candidates_cols = sudoku.possibles.find_sole_candidate(Axis.column)
        sole_candidates_nbrs = sudoku.possibles.find_sole_candidate(Axis.number)

        sudoku.add_numbers(*sole_candidates_rows)
        sudoku.add_numbers(*sole_candidates_cols)
        sudoku.add_numbers(*sole_candidates_nbrs)

    return sudoku.array
