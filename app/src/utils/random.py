from typing import Tuple

import numpy as np


def generate_bool():
    return np.random.choice([True, False])


def get_random_indices(
    matrix: np.ndarray, sample_size: np.ndarray = 1
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Takes random matrix rows without replacemenet.

    Args:
        matrix: 2d numpy array from which random will be taken.

    Returns:
        Two numpy vector representing random values from taken rows.

    """
    indices = np.random.choice(a=matrix.shape[0], size=sample_size, replace=False)
    return matrix[indices][:, 0], matrix[indices][:, 1]
