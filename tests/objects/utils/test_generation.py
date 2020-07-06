import numpy as np

from objects.utils.generation import generate_empty_sudoku, generate_empty_possibles_matrix


def test_generate_empty_sudoku_function_returns_array_with_proper_shape():
    # GIVEN
    expected_shape = (9, 9)

    # WHEN
    shape = generate_empty_sudoku().shape

    # THEN
    assert shape == expected_shape


def test_generate_empty_sudoku_return_array_with_proper_type():
    # GIVEN
    expected_array_type = np.uint8

    # WHEN
    array_type = generate_empty_sudoku().dtype

    # THEN
    assert expected_array_type == array_type


def test_generate_empty_possibles_matrix_return_array_with_proper_shape():
    # GIVEN
    expected_shape = (9, 9, 9)

    # WHEN
    shape = generate_empty_possibles_matrix().shape

    # THEN
    assert shape == expected_shape

def test_generate_empty_possibles_matrix_return_array_with_proper_type():
    # GIVEN
    expected_array_type = np.uint8

    # WHEN
    array_type = generate_empty_possibles_matrix().dtype

    # THEN
    assert  array_type == expected_array_type

