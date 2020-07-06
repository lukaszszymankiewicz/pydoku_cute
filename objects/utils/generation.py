import numpy as np
from .constants import SUDOKU_SIZE, NUMBERS_TYPE, SIDE_SIZE


def generate_empty_sudoku(size: tuple) -> np.ndarray:
    return np.zeros(shape=SUDOKU_SIZE, dtype=NUMBERS_TYPE)


def generate_empty_possibles_matrix() -> np.ndarray:
    size = slice(1, SIDE_SIZE +1)
    return np.mgrid[size, size, size][2]
