import numpy as np

from src.objects.utils import sudoku_is_valid


def test_sudoku_is_valid_validates_valid_sudoku():
    # GIVEN
    sudoku_array = np.array(
        [
            [5, 2, 1, 6, 4, 9, 8, 3, 7],
            [4, 7, 3, 8, 1, 5, 6, 2, 9],
            [6, 9, 8, 3, 2, 7, 4, 1, 5],
            [3, 6, 7, 1, 5, 2, 9, 4, 8],
            [8, 5, 4, 9, 3, 6, 1, 7, 2],
            [2, 1, 9, 7, 8, 4, 3, 5, 6],
            [1, 3, 2, 5, 6, 8, 7, 9, 4],
            [7, 4, 6, 2, 9, 3, 5, 8, 1],
            [9, 8, 5, 4, 7, 1, 2, 6, 3],
        ]
    )
    expected_validation_result = True

    # WHEN
    validation_result = sudoku_is_valid(sudoku_array)

    # THEN
    assert validation_result == expected_validation_result


def test_sudoku_is_valid_validates_invalid_sudoku():
    # GIVEN
    sudoku_array = np.array(
        [
            [5, 2, 1, 6, 4, 9, 8, 3, 7],
            [4, 7, 3, 8, 1, 5, 6, 2, 9],
            [6, 9, 8, 3, 2, 7, 4, 1, 5],
            [3, 6, 7, 1, 5, 2, 9, 4, 8],
            [8, 5, 4, 9, 3, 6, 1, 7, 2],
            [2, 1, 9, 7, 8, 4, 3, 5, 6],
            [1, 3, 2, 5, 6, 8, 7, 9, 4],
            [7, 4, 6, 2, 9, 3, 5, 8, 1],
            [9, 8, 5, 4, 7, 1, 2, 6, 1],  # <- here is error!
        ]
    )
    expected_validation_result = False

    # WHEN
    validation_result = sudoku_is_valid(sudoku_array)

    # THEN
    assert validation_result == expected_validation_result
