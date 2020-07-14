import numpy as np


def filter_zeros_from_vector(vector: np.ndarray) -> np.ndarray:
    return vector[vector != 0]
