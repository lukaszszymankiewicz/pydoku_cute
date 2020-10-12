import numpy as np
import pytest
from app.src.utils.misc import find_unique_number


@pytest.mark.parametrize(
    "vector,expected_result",
    [
        (np.array([0, 0, 0, 0]), np.array([])),
        (np.array([1, 0, 0, 0]), np.array([0])),
        (np.array([0, 2, 0, 0]), np.array([1])),
        (np.array([0, 0, 3, 0]), np.array([2])),
        (np.array([0, 0, 0, 4]), np.array([3])),
        (np.array([1, 2, 0, 0]), np.array([])),
    ],
)
def test_find_unique_number_works_properly_for_vector(vector, expected_result):
    # WHEN
    unique_numbers = find_unique_number(array=vector, axis=0)

    # THEN
    assert np.all(unique_numbers == expected_result)


@pytest.mark.parametrize(
    "matrix,expected_result",
    [
        (np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), (np.array([]), np.array([]))),
        (np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), (np.array([0]), np.array([0]))),
        (np.array([[0, 2, 0], [0, 0, 0], [0, 0, 0]]), (np.array([0]), np.array([1]))),
        (np.array([[0, 0, 3], [0, 0, 0], [0, 0, 0]]), (np.array([0]), np.array([2]))),
        (np.array([[0, 0, 0], [4, 0, 0], [0, 0, 0]]), (np.array([1]), np.array([0]))),
        (np.array([[0, 0, 0], [0, 5, 0], [0, 0, 0]]), (np.array([1]), np.array([1]))),
        (np.array([[0, 0, 0], [0, 0, 6], [0, 0, 0]]), (np.array([1]), np.array([2]))),
        (np.array([[0, 0, 0], [0, 0, 0], [7, 0, 0]]), (np.array([2]), np.array([0]))),
        (np.array([[0, 0, 0], [0, 0, 0], [0, 8, 0]]), (np.array([2]), np.array([1]))),
        (np.array([[0, 0, 0], [0, 0, 0], [0, 0, 9]]), (np.array([2]), np.array([2]))),
        (np.array([[1, 0, 0], [0, 0, 0], [0, 0, 9]]), (np.array([0, 2]), np.array([0, 2]))),
        (np.array([[0, 2, 0], [0, 0, 0], [0, 0, 9]]), (np.array([0, 2]), np.array([1, 2]))),
        (np.array([[0, 0, 0], [1, 0, 0], [0, 0, 9]]), (np.array([1, 2]), np.array([0, 2]))),
        (np.array([[0, 0, 0], [0, 2, 0], [0, 0, 9]]), (np.array([1, 2]), np.array([1, 2]))),
        (np.array([[1, 2, 0], [0, 0, 0], [0, 0, 9]]), (np.array([2]), np.array([2]))),
        (np.array([[1, 0, 0], [0, 2, 0], [0, 0, 9]]), (np.array([0, 1, 2]), np.array([0, 1, 2]))),
        (np.array([[0, 0, 0], [1, 2, 0], [0, 0, 9]]), (np.array([2]), np.array([2]))),
        (np.array([[1, 0, 3], [0, 0, 0], [1, 0, 9]]), (np.array([]), np.array([]))),
        (np.array([[1, 0, 0], [0, 0, 3], [1, 0, 9]]), (np.array([0, 1]), np.array([0, 2]))),
        (np.array([[0, 0, 0], [0, 0, 3], [0, 0, 9]]), (np.array([1, 2]), np.array([2, 2]))),
        (np.array([[0, 0, 3], [0, 0, 0], [0, 0, 9]]), (np.array([0, 2]), np.array([2, 2]))),
    ],
)
def test_find_unique_number_works_properly_for_matrix_for_axis_1(matrix, expected_result):
    # WHEN
    unique_numbers = find_unique_number(array=matrix, axis=1)

    # THEN
    for numbers, result in zip(unique_numbers, expected_result):
        assert np.all(numbers == result)


@pytest.mark.parametrize(
    "matrix,expected_result",
    [
        (np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), (np.array([]), np.array([]))),
        (np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), (np.array([0]), np.array([0]))),
        (np.array([[0, 2, 0], [0, 0, 0], [0, 0, 0]]), (np.array([0]), np.array([1]))),
        (np.array([[0, 0, 3], [0, 0, 0], [0, 0, 0]]), (np.array([0]), np.array([2]))),
        (np.array([[0, 0, 0], [4, 0, 0], [0, 0, 0]]), (np.array([1]), np.array([0]))),
        (np.array([[0, 0, 0], [0, 5, 0], [0, 0, 0]]), (np.array([1]), np.array([1]))),
        (np.array([[0, 0, 0], [0, 0, 6], [0, 0, 0]]), (np.array([1]), np.array([2]))),
        (np.array([[0, 0, 0], [0, 0, 0], [7, 0, 0]]), (np.array([2]), np.array([0]))),
        (np.array([[0, 0, 0], [0, 0, 0], [0, 8, 0]]), (np.array([2]), np.array([1]))),
        (np.array([[0, 0, 0], [0, 0, 0], [0, 0, 9]]), (np.array([2]), np.array([2]))),
        (np.array([[1, 0, 0], [0, 0, 0], [0, 0, 9]]), (np.array([0, 2]), np.array([0, 2]))),
        (np.array([[0, 2, 0], [0, 0, 0], [0, 0, 9]]), (np.array([0, 2]), np.array([1, 2]))),
        (np.array([[0, 0, 0], [1, 0, 0], [0, 0, 9]]), (np.array([1, 2]), np.array([0, 2]))),
        (np.array([[0, 0, 0], [0, 2, 0], [0, 0, 9]]), (np.array([1, 2]), np.array([1, 2]))),
        (np.array([[1, 2, 0], [0, 0, 0], [0, 0, 9]]), (np.array([0, 0, 2]), np.array([0, 1, 2]))),
        (np.array([[1, 0, 0], [0, 2, 0], [0, 0, 9]]), (np.array([0, 1, 2]), np.array([0, 1, 2]))),
        (np.array([[0, 0, 0], [1, 2, 0], [0, 0, 9]]), (np.array([1, 1, 2]), np.array([0, 1, 2]))),
        (np.array([[1, 0, 3], [0, 0, 0], [1, 0, 9]]), (np.array([]), np.array([]))),
        (np.array([[1, 0, 0], [0, 0, 3], [1, 0, 9]]), (np.array([]), np.array([]))),
        (np.array([[0, 0, 0], [0, 0, 3], [0, 0, 9]]), (np.array([]), np.array([]))),
        (np.array([[0, 0, 3], [0, 0, 0], [0, 0, 9]]), (np.array([]), np.array([]))),
    ],
)
def test_find_unique_number_works_properly_for_matrix_for_axis_0(matrix, expected_result):
    # GIVEN
    unique_numbers = find_unique_number(array=matrix, axis=0)

    # THEN
    for numbers, result in zip(unique_numbers, expected_result):
        assert np.all(numbers == result)
