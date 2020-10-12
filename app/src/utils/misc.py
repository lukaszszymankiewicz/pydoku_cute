import numpy as np

from ..constants import NUMBERS_TYPE
from ..types import Cube, Matrix, Scalar


def find_unique_number(array: Cube, axis: Scalar) -> Matrix:
    """ Finds numbers which occurs inly once in given axis.
    Args:
        array: 3d numpy array,
        axis: integer representing axis in which uniques need to be found.

    Returns:
        2d numpy array representing positions of uniques numbers in proveided array
    """

    mask = (array != 0).sum(axis=axis, keepdims=True) > 1
    candidates = np.where(mask, 0, array).astype(NUMBERS_TYPE)
    candidates_indices = np.nonzero(candidates)

    return candidates_indices
