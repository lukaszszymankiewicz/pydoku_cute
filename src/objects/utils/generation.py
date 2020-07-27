import numpy as np

from src.static.constants import NUMBERS_TYPE, SIDE_SIZE, SUDOKU_SIZE


def generate_empty_possibles_matrix() -> np.ndarray:
    size = slice(1, SIDE_SIZE + 1)
    return np.mgrid[size, size, size][2].astype(NUMBERS_TYPE)
