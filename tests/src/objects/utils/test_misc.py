import pytest

from numpy import array
from numpy import all as numpy_all


from src.objects.utils.misc import replace_values, find_unique_number


def test_replace_values_works_properly():
    # GIVEN
    sample_array = array([1, 2, 3, 4])
    sample_map = {1: 2, 2: 3, 3: 4, 4: 5}
    expected_array = array([2, 3, 4, 5])

    # WHEN
    array_after_replacing = replace_values(sample_array, sample_map)

    # THEN
    assert numpy_all(array_after_replacing == expected_array)
    assert array_after_replacing.shape == expected_array.shape


@pytest.mark.parametrize(
        "vector,expected_result",
        [
            (array([0, 0, 0, 0]), array([])),
            (array([1, 0, 0, 0]), array([0])),
            (array([0, 2, 0, 0]), array([1])),
            (array([0, 0, 3, 0]), array([2])),
            (array([0, 0, 0, 4]), array([3])),
            (array([1, 2, 0, 0]), array([])),
        ]
    )
def test_find_unique_number_works_properly_for_vector(vector, expected_result):
    # WHEN
    unique_numbers = find_unique_number(array=vector, axis=0)

    # THEN
    assert numpy_all(unique_numbers == expected_result)


@pytest.mark.parametrize(
        "matrix,expected_result",
        [
            (array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), (array([]), array([]))),
            (array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), (array([0]), array([0]))),
            (array([[0, 2, 0], [0, 0, 0], [0, 0, 0]]), (array([0]), array([1]))),
            (array([[0, 0, 3], [0, 0, 0], [0, 0, 0]]), (array([0]), array([2]))),
            (array([[0, 0, 0], [4, 0, 0], [0, 0, 0]]), (array([1]), array([0]))),
            (array([[0, 0, 0], [0, 5, 0], [0, 0, 0]]), (array([1]), array([1]))),
            (array([[0, 0, 0], [0, 0, 6], [0, 0, 0]]), (array([1]), array([2]))),
            (array([[0, 0, 0], [0, 0, 0], [7, 0, 0]]), (array([2]), array([0]))),
            (array([[0, 0, 0], [0, 0, 0], [0, 8, 0]]), (array([2]), array([1]))),
            (array([[0, 0, 0], [0, 0, 0], [0, 0, 9]]), (array([2]), array([2]))),
            (array([[1, 0, 0], [0, 0, 0], [0, 0, 9]]), (array([0, 2]), array([0, 2]))),
            (array([[0, 2, 0], [0, 0, 0], [0, 0, 9]]), (array([0, 2]), array([1, 2]))),
            (array([[0, 0, 0], [1, 0, 0], [0, 0, 9]]), (array([1, 2]), array([0, 2]))),
            (array([[0, 0, 0], [0, 2, 0], [0, 0, 9]]), (array([1, 2]), array([1, 2]))),
            (array([[1, 2, 0], [0, 0, 0], [0, 0, 9]]), (array([2]), array([2]))),
            (array([[1, 0, 0], [0, 2, 0], [0, 0, 9]]), (array([0, 1, 2]), array([0, 1, 2]))),
            (array([[0, 0, 0], [1, 2, 0], [0, 0, 9]]), (array([2]), array([2]))),
            (array([[1, 0, 3], [0, 0, 0], [1, 0, 9]]), (array([]), array([]))),
            (array([[1, 0, 0], [0, 0, 3], [1, 0, 9]]), (array([0, 1]), array([0, 2]))),
            (array([[0, 0, 0], [0, 0, 3], [0, 0, 9]]), (array([1, 2]), array([2, 2]))),
            (array([[0, 0, 3], [0, 0, 0], [0, 0, 9]]), (array([0, 2]), array([2, 2]))),
        ]
    )
def test_find_unique_number_works_properly_for_matrix_for_axis_1(matrix, expected_result):
    # WHEN
    unique_numbers = find_unique_number(array=matrix, axis=1)

    # THEN
    for numbers, result in zip(unique_numbers, expected_result):
        assert numpy_all(numbers == result)


@pytest.mark.parametrize(
        "matrix,expected_result",
        [
            (array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), (array([]), array([]))),
            (array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), (array([0]), array([0]))),
            (array([[0, 2, 0], [0, 0, 0], [0, 0, 0]]), (array([0]), array([1]))),
            (array([[0, 0, 3], [0, 0, 0], [0, 0, 0]]), (array([0]), array([2]))),
            (array([[0, 0, 0], [4, 0, 0], [0, 0, 0]]), (array([1]), array([0]))),
            (array([[0, 0, 0], [0, 5, 0], [0, 0, 0]]), (array([1]), array([1]))),
            (array([[0, 0, 0], [0, 0, 6], [0, 0, 0]]), (array([1]), array([2]))),
            (array([[0, 0, 0], [0, 0, 0], [7, 0, 0]]), (array([2]), array([0]))),
            (array([[0, 0, 0], [0, 0, 0], [0, 8, 0]]), (array([2]), array([1]))),
            (array([[0, 0, 0], [0, 0, 0], [0, 0, 9]]), (array([2]), array([2]))),
            (array([[1, 0, 0], [0, 0, 0], [0, 0, 9]]), (array([0, 2]), array([0, 2]))),
            (array([[0, 2, 0], [0, 0, 0], [0, 0, 9]]), (array([0, 2]), array([1, 2]))),
            (array([[0, 0, 0], [1, 0, 0], [0, 0, 9]]), (array([1, 2]), array([0, 2]))),
            (array([[0, 0, 0], [0, 2, 0], [0, 0, 9]]), (array([1, 2]), array([1, 2]))),
            (array([[1, 2, 0], [0, 0, 0], [0, 0, 9]]), (array([0, 0, 2]), array([0, 1, 2]))),
            (array([[1, 0, 0], [0, 2, 0], [0, 0, 9]]), (array([0, 1, 2]), array([0, 1, 2]))),
            (array([[0, 0, 0], [1, 2, 0], [0, 0, 9]]), (array([1, 1, 2]), array([0, 1, 2]))),
            (array([[1, 0, 3], [0, 0, 0], [1, 0, 9]]), (array([]), array([]))),
            (array([[1, 0, 0], [0, 0, 3], [1, 0, 9]]), (array([]), array([]))),
            (array([[0, 0, 0], [0, 0, 3], [0, 0, 9]]), (array([]), array([]))),
            (array([[0, 0, 3], [0, 0, 0], [0, 0, 9]]), (array([]), array([]))),
        ]
    )
def test_find_unique_number_works_properly_for_matrix_for_axis_0(matrix, expected_result):
    # GIVEN
    unique_numbers = find_unique_number(array=matrix, axis=0)

    # THEN
    for numbers, result in zip(unique_numbers, expected_result):
        assert numpy_all(numbers == result)
