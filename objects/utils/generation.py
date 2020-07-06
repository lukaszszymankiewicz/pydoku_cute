import numpy as np


def generate_empty_sudoku(size: tuple) -> np.ndarray:
    return np.zeros(shape=size, dtype=np.uint8)


def generate_empty_possibles_matrix() -> np.ndarray:
    size = slice(1, 10)
    return np.mgrid[size, size, size][2]
