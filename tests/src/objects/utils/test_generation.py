import numpy as np

from src.objects.utils import generate_empty_possibles_matrix


def test_generate_empty_possibles_matrix_retuns_proper_shaped_matrix():
    # GIVEN
    expected_shape = (9, 9, 9)

    # WHEN
    possibles_matrix = generate_empty_possibles_matrix()

    # THEN
    assert possibles_matrix.shape == expected_shape


def test_generate_empty_possibles_matrix_returns_array_with_proper_dtype():
    # GIVEN
    expected_dtype = np.uint8

    # WHEN
    dtype = generate_empty_possibles_matrix().dtype 

    # THEN
    assert dtype == expected_dtype


def test_generate_empty_possibles_matrix_returns_proper_matrix_in_shape_2():
    # GIVEN
    expected_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # WHEN
    possibles_matrix = generate_empty_possibles_matrix()

    # THEN
    for row in range(9):
        for col in range(9):
            assert np.all(possibles_matrix[row, col] == expected_values)


def test_generate_empty_possibles_matrix_returns_proper_matrix_in_shape_1():
    # GIVEN
    expected_values = np.array(
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ]
    )

    # WHEN
    possibles_matrix = generate_empty_possibles_matrix()

    # THEN
    for row in range(9):
        assert np.all(possibles_matrix[row] == expected_values)
        assert np.all(possibles_matrix[:, row] == expected_values)


def test_generate_empty_possibles_matrix_returns_proper_matrix_in_shape_0():
    # WHEN
    possibles_matrix = generate_empty_possibles_matrix()

    # THEN
    for number in range(9):
        assert np.all(possibles_matrix[:, :, number] == np.zeros((9, 9)) + number + 1)
