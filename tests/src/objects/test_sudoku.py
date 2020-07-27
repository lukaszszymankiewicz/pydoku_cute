import numpy as np
import pytest

from src.objects.sudoku import Sudoku


def test_initialization_of_notempty_sudoku_object_returns_proper_object():
    # GIVEN
    sample_array = np.random.randint(low=0, high=10, size=((9, 9)))
    expected_dtype = np.uint8
    expected_params = ["array", "_possibles"]
    expected_shape = (9, 9)

    # WHEN
    sudoku_object = Sudoku(sample_array)

    # THEN
    for param in expected_params:
        assert hasattr(sudoku_object, param)

    assert sudoku_object.array.dtype == expected_dtype
    assert sudoku_object.array.shape == expected_shape


def test_where_is_empty_property_works_properly():
    # GIVEN
    sample_array = np.array([[1, 2, 3], [0, 2, 3], [1, 2, 0],])
    expected_where_is_empty = np.array([[1, 0], [2, 2]])

    # WHEN
    sudoku = Sudoku(sample_array)

    # THEN
    assert np.all(sudoku.where_is_empty == expected_where_is_empty)


def test_where_is_filled_property_works_properly():
    # GIVEN
    sample_array = np.array([[0, 0, 0], [0, 2, 0], [1, 0, 0],])
    expected_where_is_empty = np.array([[1, 1], [2, 0]])

    # WHEN
    sudoku = Sudoku(sample_array)

    # THEN
    assert np.all(sudoku.where_is_filled == expected_where_is_empty)


def test_where_is_solved_property_works_properly_for_not_solved_sudoku():
    # GIVEN
    sample_array = np.array([[0, 0, 0], [0, 2, 0], [1, 0, 0],])
    expected_result = False

    # WHEN
    sudoku = Sudoku(sample_array)

    # THEN
    assert sudoku.is_solved == expected_result


def test_where_is_solved_property_works_properly_for_solved_sudoku():
    # GIVEN
    sample_array = np.array([[1, 2, 3], [3, 1, 2], [2, 3, 1],])
    expected_result = True

    # WHEN
    sudoku = Sudoku(sample_array)

    # THEN
    assert sudoku.is_solved == expected_result


def test_filled_rows_property_works_properly():
    # GIVEN
    sample_array = np.array([[0, 0, 0], [0, 2, 0], [1, 0, 0],])
    expected_filled_rows = np.array([1, 2])

    # WHEN
    sudoku = Sudoku(sample_array)

    # THEN
    assert np.all(sudoku.filled_rows == expected_filled_rows)


def test_filled_columns_property_works_properly():
    # GIVEN
    sample_array = np.array([[0, 0, 0], [0, 2, 0], [1, 0, 0],])
    expected_filled_columns = np.array([1, 0])

    # WHEN
    sudoku = Sudoku(sample_array)

    # THEN
    assert np.all(sudoku.filled_columns == expected_filled_columns)


def test_filled_numbers_property_works_properly():
    # GIVEN
    sample_array = np.array([[0, 0, 0], [0, 5, 0], [1, 0, 0],])
    expected_filled_numbers = np.array([5, 1])

    # WHEN
    sudoku = Sudoku(sample_array)

    # THEN
    assert np.all(sudoku.filled_numbers + 1 == expected_filled_numbers)


def test_copy_funkction_works_properly():
    # GIVEN
    sample_array = np.array([[0, 0, 0], [0, 5, 0], [1, 0, 0],])
    sample_sudoku = Sudoku(sample_array)

    # WHEN
    copied_sudoku = sample_sudoku.copy()

    # THEN
    assert np.all(copied_sudoku.array == sample_sudoku.array)
    assert np.all(copied_sudoku._possibles.matrix == sample_sudoku._possibles.matrix)


def test_copy_function_return_independent_copy():
    # GIVEN
    sample_array = np.array([[0, 0, 0], [0, 5, 0], [1, 0, 0],])
    sample_sudoku = Sudoku(sample_array)

    # WHEN
    copied_sudoku = sample_sudoku.copy()
    copied_sudoku[0, 0] = 5
    copied_sudoku.update()

    # THEN
    assert np.any(copied_sudoku.array != sample_sudoku.array)
    assert np.any(copied_sudoku._possibles.matrix != sample_sudoku._possibles.matrix)


def test_get_most_promising_cell_works_properly():
    # GIVEN
    sample_array = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
        ]
    )
    expected_indices = (1, 5)

    # WHEN
    sudoku = Sudoku(sample_array)
    sudoku.update()
    indices = sudoku.get_most_promising_cell()

    # THEN
    assert indices == expected_indices


@pytest.mark.parametrize(
    "indices,expected_numbers",
    [
        ((0, 0), np.array([])),
        ((0, 1), np.array([4, 5, 6, 7, 8, 9])),
        ((0, 2), np.array([4, 5, 6, 7, 8, 9])),
        ((0, 3), np.array([2, 3, 5, 6, 7, 8, 9])),
        ((0, 4), np.array([2, 3, 4, 6, 7, 8, 9])),
        ((0, 5), np.array([2, 3, 4, 5, 7, 9])),
        ((0, 6), np.array([2, 3, 4, 5, 6, 7, 9])),
        ((0, 7), np.array([2, 3, 4, 5, 6, 8, 9])),
        ((0, 8), np.array([2, 3, 4, 5, 6, 7, 8])),
        ((1, 0), np.array([4, 5, 6, 7, 8, 9])),
        ((1, 1), np.array([])),
        ((1, 2), np.array([4, 5, 6, 7, 8, 9])),
        ((1, 3), np.array([3, 5, 6, 7, 8, 9])),
        ((1, 4), np.array([3, 4, 6, 7, 8, 9])),
        ((1, 5), np.array([3, 4, 5, 7, 9])),
        ((1, 6), np.array([3, 4, 5, 6, 7, 9])),
        ((1, 7), np.array([3, 4, 5, 6, 8, 9])),
        ((1, 8), np.array([])),
        ((2, 0), np.array([4, 5, 6, 7, 8, 9])),
        ((2, 1), np.array([4, 5, 6, 7, 8, 9])),
        ((2, 2), np.array([])),
        ((2, 3), np.array([1, 2, 5, 6, 7, 8, 9])),
        ((2, 4), np.array([1, 2, 4, 6, 7, 8, 9])),
        ((2, 5), np.array([1, 2, 4, 5, 7, 9])),
        ((2, 6), np.array([2, 4, 5, 6, 7, 9])),
        ((2, 7), np.array([2, 4, 5, 6, 8, 9])),
        ((2, 8), np.array([2, 4, 5, 6, 7, 8])),
        ((3, 0), np.array([2, 3, 5, 6, 7, 8, 9])),
        ((3, 1), np.array([1, 3, 5, 6, 7, 8, 9])),
        ((3, 2), np.array([1, 2, 5, 6, 7, 8, 9])),
        ((3, 3), np.array([])),
        ((3, 4), np.array([1, 2, 3, 7, 9])),
        ((3, 5), np.array([1, 2, 3, 7, 9])),
        ((3, 6), np.array([1, 2, 3, 5, 6, 7, 9])),
        ((3, 7), np.array([1, 2, 3, 5, 6, 8, 9])),
        ((3, 8), np.array([2, 3, 5, 6, 7, 8])),
        ((4, 0), np.array([2, 3, 4, 6, 7, 9])),
        ((4, 1), np.array([1, 3, 4, 6, 7, 9])),
        ((4, 2), np.array([1, 2, 4, 6, 7, 9])),
        ((4, 3), np.array([1, 2, 3, 7, 9])),
        ((4, 4), np.array([])),
        ((4, 5), np.array([])),
        ((4, 6), np.array([1, 2, 3, 4, 6, 7, 9])),
        ((4, 7), np.array([1, 2, 3, 4, 6, 9])),
        ((4, 8), np.array([2, 3, 4, 6, 7])),
        ((5, 0), np.array([2, 3, 4, 5, 7, 8, 9])),
        ((5, 1), np.array([1, 3, 4, 5, 7, 8, 9])),
        ((5, 2), np.array([1, 2, 4, 5, 7, 8, 9])),
        ((5, 3), np.array([1, 2, 3, 7, 9])),
        ((5, 4), np.array([1, 2, 3, 7, 9])),
        ((5, 5), np.array([])),
        ((5, 6), np.array([1, 2, 3, 4, 5, 7, 9])),
        ((5, 7), np.array([1, 2, 3, 4, 5, 8, 9])),
        ((5, 8), np.array([2, 3, 4, 5, 7, 8])),
        ((6, 0), np.array([2, 3, 4, 5, 6, 7, 9])),
        ((6, 1), np.array([1, 3, 4, 5, 6, 7, 9])),
        ((6, 2), np.array([1, 2, 4, 5, 6, 7, 9])),
        ((6, 3), np.array([1, 2, 3, 5, 6, 7, 9])),
        ((6, 4), np.array([1, 2, 3, 4, 6, 7, 9])),
        ((6, 5), np.array([1, 2, 3, 4, 5, 7, 9])),
        ((6, 6), np.array([])),
        ((6, 7), np.array([1, 2, 3, 4, 5, 6])),
        ((6, 8), np.array([2, 3, 4, 5, 6])),
        ((7, 0), np.array([2, 3, 4, 5, 6, 8, 9])),
        ((7, 1), np.array([1, 3, 4, 5, 6, 8, 9])),
        ((7, 2), np.array([1, 2, 4, 5, 6, 8, 9])),
        ((7, 3), np.array([1, 2, 3, 5, 6, 8, 9])),
        ((7, 4), np.array([1, 2, 3, 4, 6, 8, 9])),
        ((7, 5), np.array([1, 2, 3, 4, 5, 9])),
        ((7, 6), np.array([1, 2, 3, 4, 5, 6])),
        ((7, 7), np.array([])),
        ((7, 8), np.array([2, 3, 4, 5, 6])),
        ((8, 0), np.array([2, 3, 4, 5, 6, 7, 8])),
        ((8, 1), np.array([1, 3, 4, 5, 6, 7, 8])),
        ((8, 2), np.array([1, 2, 4, 5, 6, 7, 8])),
        ((8, 3), np.array([1, 2, 3, 5, 6, 7, 8])),
        ((8, 4), np.array([1, 2, 3, 4, 6, 7, 8])),
        ((8, 5), np.array([1, 2, 3, 4, 5, 7])),
        ((8, 6), np.array([1, 2, 3, 4, 5, 6])),
        ((8, 7), np.array([1, 2, 3, 4, 5, 6])),
        ((8, 8), np.array([])),
    ],
)
def test_get_possible_numbers_works_properly(indices, expected_numbers):
    # GIVEN
    sample_array = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
        ]
    )

    # WHEN
    sudoku = Sudoku(sample_array)
    sudoku.update()
    indices = sudoku.get_possible_numbers(*indices)

    # THEN
    assert np.all(indices == expected_numbers)


def test_get_sudoku_combinations_works_properly():
    sample_array = np.array([[0, 0, 0], [0, 5, 0], [1, 0, 0],])
    sudoku = Sudoku(sample_array)
    row = 0
    col = 0
    values = np.array([1, 2])

    expected_sudoku_combinations = [
        Sudoku(np.array([[1, 0, 0], [0, 5, 0], [1, 0, 0],])),
        Sudoku(np.array([[2, 0, 0], [0, 5, 0], [1, 0, 0],])),
    ]

    # WHEN
    sudoku_combinations = sudoku.get_sudoku_combinations(row, col, values)

    # THEN
    for expected, generated in zip(expected_sudoku_combinations, sudoku_combinations):
        assert np.all(expected.array == generated.array)
