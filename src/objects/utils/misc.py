from src.static.constants import NUMBERS_TYPE
from src.static.types import Cube, Scalar, Matrix
from numpy import where, nonzero


def find_unique_number(array: Cube, axis: Scalar) -> Matrix:
    mask = (array != 0).sum(axis=axis, keepdims=True) > 1
    candidates = where(mask, 0, array).astype(NUMBERS_TYPE)
    candidates_indices = nonzero(candidates)

    return candidates_indices
