import numpy as np

from ..constants import NUMBERS_TYPE, SIDE_SIZE
from ..types import Cube


def generate_empty_possibles_matrix() -> Cube:
    """Generates 3d numpy array representing empty sudoku possibles in every cell."""

    size = slice(1, SIDE_SIZE + 1)
    return np.mgrid[size, size, size][2].astype(NUMBERS_TYPE)
