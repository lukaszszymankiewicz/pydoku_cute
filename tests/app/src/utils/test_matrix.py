import numpy as np
import pytest
from app.src.utils.matrix import find_least_filled_place_in_matrix, get_matrix_combinations


def test_find_the_least_occuring_element_in_matrix_works_properly_for_simple_case():
    # GIVEN
    sample_matrix = np.array(
        [
            [[1, 0, 0], [1, 0, 0], [0, 0, 1],],
            [[2, 0, 0], [2, 0, 0], [0, 0, 2],],
            [[3, 0, 0], [3, 0, 0], [0, 0, 0],],
        ]
    )

    expected_indices = (0, 0)

    # WHEN
    indices = find_least_filled_place_in_matrix(sample_matrix)

    # THEN
    assert indices == expected_indices


def test_find_the_least_occuring_element_in_matrix_works_properly_equal_counts_case():

    """
    Because testing function shows the axis 2 least filled place, it should properly show these 
    place if there is other same occurance counts in matrix. Algorithm in finding it is "naive"
    so always the indices closer to zero will be chosed (as this test shows).
    
    Both [0, 0] and [2, 2] indices of a matrix has same number of nonzero elements in it, but
    algorithm will always choose lower ones (or first occurance).
    """
    # GIVEN
    sample_matrix = np.array(
        [
            [[1, 0, 0], [0, 0, 0], [0, 0, 1],],
            [[2, 0, 0], [0, 0, 0], [0, 0, 2],],
            [[3, 0, 0], [0, 0, 0], [0, 0, 3],],
        ]
    )

    expected_indices = np.array([0]), np.array([0])

    # WHEN
    indices = find_least_filled_place_in_matrix(sample_matrix)

    # THEN
    for index, expected_index in zip(indices, expected_indices):
        assert np.all(index == expected_index)


def test_find_the_least_occuring_element_in_matrix_works_properly_for_empty_matrix():
    # GIVEN
    sample_matrix = np.array(
        [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0],],
        ]
    )

    # WHEN & WHEN
    with pytest.raises(IndexError):
        find_least_filled_place_in_matrix(sample_matrix)


def test_get_matrix_combinations_works_properly():
    # GIVEN
    sample_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0],],)
    row = 0
    col = 0
    values = np.array([1, 2, 3])
    expected_number_of_matrix_combinations = 3

    expected_matrix_combinations = [
        np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0],],),
        np.array([[2, 0, 0], [0, 0, 0], [0, 0, 0],],),
        np.array([[3, 0, 0], [0, 0, 0], [0, 0, 0],],),
    ]
    # WHEN
    matrix_combinations = get_matrix_combinations(sample_matrix, row, col, values)

    # THEN
    for combination, expected_matrix in zip(matrix_combinations, expected_matrix_combinations):
        assert np.all(combination == expected_matrix)
