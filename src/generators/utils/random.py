import numpy as np


def get_random_indices(matrix: np.ndarray, sample_size: int=1):
    indices = np.random.choice(a=matrix.shape[0], size=sample_size, replace=False)
    return matrix[indices][:, 0], matrix[indices][:, 1]
