from typing import Tuple
from src.static.types import Matrix, Scalar, Vector
from numpy.random import choice


def get_random_indices(matrix: Matrix, sample_size: Scalar= 1) -> Tuple[Vector, Vector]:
    indices = choice(a=matrix.shape[0], size=sample_size, replace=False)
    return matrix[indices][:, 0], matrix[indices][:, 1]
