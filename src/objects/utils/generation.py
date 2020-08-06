from numpy import mgrid

from src.static.types import Cube
from src.static.constants import NUMBERS_TYPE, SIDE_SIZE, SUDOKU_SIZE


def generate_empty_possibles_matrix() -> Cube:
    size = slice(1, SIDE_SIZE + 1)
    return mgrid[size, size, size][2].astype(NUMBERS_TYPE)
