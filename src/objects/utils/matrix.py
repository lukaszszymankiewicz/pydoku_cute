from typing import Tuple, List

from numpy import count_nonzero, argwhere, unique, copy

from src.static.types import Matrix, Index, Index, Vector


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
    counts = count_nonzero(matrix, axis=-1)
    indices = argwhere(counts == unique(counts)[1])[0]
    return indices[0], indices[1]


def get_matrix_combinations(matrix: Matrix, row: Index, col: Index, values: Vector) -> List[Matrix]:
    matrix_combinations = []

    for value in values:
        new_matrix = copy(matrix)
        new_matrix[row, col] = value
        matrix_combinations.append(new_matrix)

    return matrix_combinations
