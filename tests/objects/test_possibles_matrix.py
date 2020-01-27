import numpy as np
import pytest
from pydoku.objects import NonzeroNumbers
from pydoku.objects import PossiblesMatrix
from pydoku.objects import Sudoku


def test_creating_of_possibles_matrix_works_properly(sample_sudoku_2x2):
    # GIVEN
    expected_side = 4
    expected_square_side = 2
    expected_array = np.array(
        [
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
        ]
    )
    expected_square_side_type = np.int64

    # WHEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)

    # THEN
    assert possibles.side == expected_side
    assert possibles.square_size == expected_square_side
    assert np.all(possibles.array == expected_array)
    assert type(possibles.square_size) == expected_square_side_type


def test_cross_out_all_numbers_from_position_works_properly(sample_sudoku_2x2):
    # GIVEN
    expected_array = np.array(
        [
            [[0, 0, 0, 0], [1, 2, 3, 4], [1, 2, 3, 4], [0, 0, 0, 0]],
            [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 4]],
            [[0, 0, 0, 0], [1, 2, 3, 4], [1, 2, 3, 4], [0, 0, 0, 0]],
        ]
    )

    # WHEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    sudoku = Sudoku(sample_sudoku_2x2)
    nonzeros = NonzeroNumbers(sudoku)

    possibles.cross_out_all_numbers_from_position(nonzeros)

    # THEN
    assert np.all(possibles.array == expected_array)


def test_cross_out_numbers_from_columns_works_properly(sample_sudoku_2x2):
    # GIVEN
    expected_array = np.array(
        [
            [[0, 0, 3, 4], [0, 0, 3, 4], [0, 0, 3, 4], [0, 0, 3, 4]],
            [[1, 2, 0, 0], [1, 2, 0, 0], [1, 2, 0, 0], [1, 2, 0, 0]],
            [[0, 0, 3, 4], [0, 0, 3, 4], [0, 0, 3, 4], [0, 0, 3, 4]],
            [[1, 2, 0, 0], [1, 2, 0, 0], [1, 2, 0, 0], [1, 2, 0, 0]],
        ]
    )

    # WHEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    sudoku = Sudoku(sample_sudoku_2x2)
    nonzeros = NonzeroNumbers(sudoku)

    possibles.cross_out_numbers_from_columns(nonzeros)

    # THEN
    assert np.all(possibles.array == expected_array)


def test_cross_out_numbers_from_rows_works_properly(sample_sudoku_2x2):
    # GIVEN
    expected_array = np.array(
        [
            [[1, 0, 0, 4], [1, 0, 3, 0], [0, 2, 0, 4], [0, 2, 3, 0]],
            [[1, 0, 0, 4], [1, 0, 3, 0], [0, 2, 0, 4], [0, 2, 3, 0]],
            [[1, 0, 0, 4], [1, 0, 3, 0], [0, 2, 0, 4], [0, 2, 3, 0]],
            [[1, 0, 0, 4], [1, 0, 3, 0], [0, 2, 0, 4], [0, 2, 3, 0]],
        ]
    )

    # WHEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    sudoku = Sudoku(sample_sudoku_2x2)
    nonzeros = NonzeroNumbers(sudoku)

    possibles.cross_out_numbers_from_rows(nonzeros)

    # THEN
    assert np.all(possibles.array == expected_array)


def test_cross_out_numbers_from_squares_works_properly(sample_sudoku_2x2):
    # GIVEN
    expected_array = np.array(
        [
            [[1, 0, 3, 0], [1, 0, 3, 0], [0, 2, 0, 4], [0, 2, 0, 4]],
            [[1, 0, 3, 0], [1, 0, 3, 0], [0, 2, 0, 4], [0, 2, 0, 4]],
            [[1, 0, 0, 4], [1, 0, 0, 4], [0, 2, 3, 0], [0, 2, 3, 0]],
            [[1, 0, 0, 4], [1, 0, 0, 4], [0, 2, 3, 0], [0, 2, 3, 0]],
        ]
    )

    # WHEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    sudoku = Sudoku(sample_sudoku_2x2)
    nonzeros = NonzeroNumbers(sudoku)

    possibles.cross_out_numbers_from_squares(nonzeros)

    # THEN
    assert np.all(possibles.array == expected_array)


@pytest.mark.parametrize(
    "number,expected_row_index,expected_col_index", [(0, 0, 1), (1, 0, 1), (2, 2, 3), (3, 2, 3)],
)
def test_square_indices_works_properly_for_2x2_sudoku(
    sample_sudoku_2x2, number, expected_row_index, expected_col_index
):
    # GIVEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    expected_square_indices = np.array([expected_row_index, expected_col_index])

    # WHEN
    square_indices = possibles.square_indices(number)

    # THEN
    assert np.all(square_indices == expected_square_indices)


@pytest.mark.parametrize("row,expected_row", [(0, [0, 1]), (1, [0, 1]), (2, [2, 3]), (3, [2, 3]),])
@pytest.mark.parametrize("col,expected_col", [(0, [0, 1]), (1, [0, 1]), (2, [2, 3]), (3, [2, 3]),])
@pytest.mark.parametrize("number,expected_number", [(0, [0]), (1, [1]), (2, [2]), (3, [3]),])
def test_get_square_indices_works_properly_for_2x2_sudoku(
    row, col, number, expected_row, expected_col, expected_number, sample_sudoku_2x2
):
    # GIVEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    expected_square_indices = np.ix_(expected_row, expected_col, expected_number)

    # WHEN
    square_indices = possibles.get_square_indices(row, col, number)

    # THEN
    for result, expected_result in zip(square_indices, expected_square_indices):
        assert np.all(result == expected_result)


@pytest.mark.parametrize(
    "number,expected_indices",
    [
        (0, [0, 1, 2]),
        (1, [0, 1, 2]),
        (2, [0, 1, 2]),
        (3, [3, 4, 5]),
        (4, [3, 4, 5]),
        (5, [3, 4, 5]),
        (6, [6, 7, 8]),
        (7, [6, 7, 8]),
        (8, [6, 7, 8]),
    ],
)
def test_square_indices_works_properly_for_3x3_sudoku(sample_sudoku_3x3, number, expected_indices):
    # GIVEN
    possibles = PossiblesMatrix(sample_sudoku_3x3)
    expected_square_indices = np.array(expected_indices)

    # WHEN
    square_indices = possibles.square_indices(number)

    # THEN
    assert np.all(square_indices == expected_square_indices)


@pytest.mark.parametrize(
    "row,expected_row",
    [
        (0, [0, 1, 2]),
        (1, [0, 1, 2]),
        (2, [0, 1, 2]),
        (3, [3, 4, 5]),
        (4, [3, 4, 5]),
        (5, [3, 4, 5]),
        (6, [6, 7, 8]),
        (7, [6, 7, 8]),
        (8, [6, 7, 8]),
    ],
)
@pytest.mark.parametrize(
    "col,expected_col",
    [
        (0, [0, 1, 2]),
        (1, [0, 1, 2]),
        (2, [0, 1, 2]),
        (3, [3, 4, 5]),
        (4, [3, 4, 5]),
        (5, [3, 4, 5]),
        (6, [6, 7, 8]),
        (7, [6, 7, 8]),
        (8, [6, 7, 8]),
    ],
)
@pytest.mark.parametrize(
    "number,expected_number",
    [(0, [0]), (1, [1]), (2, [2]), (3, [3]), (4, [4]), (5, [5]), (6, [6]), (7, [7]), (8, [8]),],
)
def test_get_square_indices_works_properly_for_3x3_sudoku(
    row, col, number, expected_row, expected_col, expected_number, sample_sudoku_3x3
):
    # GIVEN
    possibles = PossiblesMatrix(sample_sudoku_3x3)
    expected_square_indices = np.ix_(expected_row, expected_col, expected_number)

    # WHEN
    square_indices = possibles.get_square_indices(row, col, number)

    # THEN
    for result, expected_result in zip(square_indices, expected_square_indices):
        assert np.all(result == expected_result)


def test_cross_out_numbers_from_square_indices_works_out_properly(sample_sudoku_2x2):
    # GIVEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    sudoku = Sudoku(sample_sudoku_2x2)
    nonzeros = NonzeroNumbers(sudoku)

    expected_possibles = np.array(
        [
            [[1, 0, 3, 0], [1, 0, 3, 0], [0, 2, 0, 4], [0, 2, 0, 4]],
            [[1, 0, 3, 0], [1, 0, 3, 0], [0, 2, 0, 4], [0, 2, 0, 4]],
            [[1, 0, 0, 4], [1, 0, 0, 4], [0, 2, 3, 0], [0, 2, 3, 0]],
            [[1, 0, 0, 4], [1, 0, 0, 4], [0, 2, 3, 0], [0, 2, 3, 0]],
        ]
    )

    # WHEN
    possibles.cross_out_numbers_from_squares(nonzeros)

    # THEN
    assert np.all(possibles.array == expected_possibles)


def test_lonely_numbers_works_in_axis_2(sample_sudoku_2x2):
    # GIVEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    sudoku = Sudoku(sample_sudoku_2x2)
    nonzeros = NonzeroNumbers(sudoku)

    possibles.cross_out_all_numbers_from_position(nonzeros)
    possibles.cross_out_numbers_from_columns(nonzeros)
    possibles.cross_out_numbers_from_rows(nonzeros)
    possibles.cross_out_numbers_from_squares(nonzeros)

    expected_lonely_numbers = np.array([[0, 3, 4, 0], [1, 0, 0, 2], [4, 0, 0, 3], [0, 1, 2, 0]])

    # WHEN
    lonely_numbers = possibles.lonely_numbers(axis=2)

    # THEN
    assert np.all(expected_lonely_numbers == lonely_numbers)


def test_lonely_numbers_works_in_axis_1(sample_sudoku_2x2):
    # GIVEN
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    sudoku = Sudoku(sample_sudoku_2x2)
    nonzeros = NonzeroNumbers(sudoku)

    possibles.cross_out_all_numbers_from_position(nonzeros)
    possibles.cross_out_numbers_from_columns(nonzeros)
    possibles.cross_out_numbers_from_rows(nonzeros)
    possibles.cross_out_numbers_from_squares(nonzeros)

    expected_lonely_numbers = np.array([[0, 3, 4, 0], [1, 0, 0, 2], [4, 0, 0, 3], [0, 1, 2, 0]])

    # WHEN
    lonely_numbers = possibles.lonely_numbers(axis=1)

    # THEN
    assert np.all(expected_lonely_numbers == lonely_numbers)


def test_lonely_numbers_works_in_axis_0(sample_sudoku_2x2):
    # GIVEN
    sudoku = Sudoku(sample_sudoku_2x2)
    possibles = PossiblesMatrix(sample_sudoku_2x2)
    nonzeros = NonzeroNumbers(sudoku)

    possibles.cross_out_all_numbers_from_position(nonzeros)
    possibles.cross_out_numbers_from_columns(nonzeros)
    possibles.cross_out_numbers_from_rows(nonzeros)
    possibles.cross_out_numbers_from_squares(nonzeros)

    expected_lonely_numbers = np.array([[0, 3, 4, 0], [1, 0, 0, 2], [4, 0, 0, 3], [0, 1, 2, 0]])

    # WHEN
    lonely_numbers = possibles.lonely_numbers(axis=0)

    # THEN
    assert np.all(expected_lonely_numbers == lonely_numbers)
