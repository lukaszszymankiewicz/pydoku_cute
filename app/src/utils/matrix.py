from typing import List, Tuple

import numpy as np

from ..types import Index, Matrix, Vector


def find_least_filled_place_in_matrix(matrix: Matrix) -> Tuple[Index, Index]:
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
    indices = np.argwhere(counts == np.unique(counts)[1])[0]
    return indices[0], indices[1]


def get_matrix_combinations(matrix: Matrix, row: Index, col: Index, values: Vector) -> List[Matrix]:
    """
    Takes matrix and several combinations. Each combinations differs from one another only by one
    value in one position of the matrix.

    Args:
        matrix - 2d numpy array from which combinations will be made,
        row - position of number which will differ in every combination,
        col - position of number which will differ in every combination,
        values - list of integer numbers. Number of combination is equal of number of provided
            values. Each combination will have differenet value from this list in (row, col)
            position

    Returns:
        List of 2d numpy arrays
    """
    matrix_combinations = []

    for value in values:
        new_matrix = np.copy(matrix)
        new_matrix[row, col] = value
        matrix_combinations.append(new_matrix)

    return matrix_combinations
