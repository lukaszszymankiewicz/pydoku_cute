import numpy as np

from objects import Sudoku
from objects.utils.enums import Axis


def solve(array: np.ndarray) -> np.ndarray:
    sudoku = Sudoku(array)

    while sudoku.is_not_solved:
        sudoku.update_possibilities()

        sole_candidates_nbrs = sudoku.possibles.find_sole_candidate(Axis.number)
        sole_candidates_rows = sudoku.possibles.find_sole_candidate(Axis.row)
        sole_candidates_cols = sudoku.possibles.find_sole_candidate(Axis.column)
    
        sole_candidates = sole_candidates_nbrs | sole_candidates_rows | sole_candidates_cols

        sudoku.add_numbers(sole_candidates)

    print(sudoku.array)
    return sudoku.array
