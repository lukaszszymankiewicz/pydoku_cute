import numpy as np

from ..constants import NUMBERS_TYPE
from ..types import Cube, Matrix, Scalar


def find_unique_number(array: Cube, axis: Scalar) -> Matrix:
    mask = (array != 0).sum(axis=axis, keepdims=True) > 1
    candidates = np.where(mask, 0, array).astype(NUMBERS_TYPE)
    candidates_indices = np.nonzero(candidates)

    return candidates_indices
