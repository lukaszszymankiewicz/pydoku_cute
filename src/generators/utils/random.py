from typing import Tuple
from src.static.types import Matrix, Scalar, Vector
from numpy.random import choice


def get_random_indices(matrix: Matrix, sample_size: Scalar= 1) -> Tuple[Vector, Vector]:
    """
    Takes random matrix rows without replacemenet.

    Args:
        matrix: 2d numpy array from which random will be taken.

    Returns:
        Two numpy vector representing random values from taken rows.

    """
    indices = choice(a=matrix.shape[0], size=sample_size, replace=False)
    return matrix[indices][:, 0], matrix[indices][:, 1]
