import numpy as np


def find_the_least_occuring_element_in_matrix(matrix: np.ndarray) -> np.ndarray:
    """
        Finds indices of row (or last dimension) which has the least non-zero elements.
    Function is using numpy unique to count occurances of non-zero elements in every cell, then 
    second element is taken (indexed as one) is taken (cause zero will be the most occuring, so
    next after zero argument needs to be taken).
        Numpy arghwere is returning tuple of results, so simple unpacking on the end is perfomed.

    Args:
        matrix: multidimensional numpy array

    Returns:
        numpy array containing indices of most-empty row (or last dimension)
    """
    counts = np.count_nonzero(matrix, axis=-1)
    return np.argwhere(counts == np.unique(counts)[1])[0]


def create_matrix_combinations_with_one_changed_value(
    matrix:np.ndarray, indices:np.ndarray, values:np.ndarray
):
    matrix_combinations = []

    for value in values:
        new_matrix = np.copy(matrix)
        new_matrix[tuple(indices)] = value
        matrix_combinations.append(new_matrix)

    return matrix_combinations
