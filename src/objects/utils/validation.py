import numpy as np


def sudoku_is_valid(array: np.ndarray) -> bool:
    for row in array:
        row = row[row > 0]
        if np.any(np.bincount(row) > 1):
            return False

    for col in array.T:
        col = col[col > 0]
        if np.any(np.bincount(col) > 1):
            return False

    return True
