import numpy as np

from pydoku.objects import NonzeroNumbers
from pydoku.objects import Sudoku


def test_creation_of_nonzero_object_works_properly():
    # GIVEN
    sample_sudoku = np.array([[0, 1], [0, 0], [2, 2], [3, 7]])
    expected_indices = [np.array([0, 2, 2, 3, 3]), np.array([1, 0, 1, 0, 1])]
    expected_numbers = np.array([0, 1, 1, 2, 6])
    expected_square_size = 2
    expected_square_size_type = np.int64

    # WHEN
    sudoku = Sudoku(sample_sudoku)
    nonzero = NonzeroNumbers(sudoku)

    indices = nonzero.indices
    numbers = nonzero.numbers
    square_size = nonzero.square_size

    # THEN
    for index, expected_index in zip(indices, expected_indices):
        assert np.all(index == expected_index)

    assert np.all(numbers == expected_numbers)
    assert square_size == expected_square_size
    assert type(square_size) == expected_square_size_type


def test_rows_property_works_properly():
    # GIVEN
    sample_sudoku = np.array([[0, 1], [0, 0], [2, 2], [3, 7]])
    expected_rows = np.array([0, 2, 2, 3, 3])

    # WHEN
    sudoku = Sudoku(sample_sudoku)
    nonzero = NonzeroNumbers(sudoku)
    rows = nonzero.rows

    # THEN
    assert np.all(rows == expected_rows)


def test_columns_property_works_properly():
    # GIVEN
    sample_sudoku = np.array([[0, 1], [0, 0], [2, 2], [3, 7]])
    expected_columns = np.array([1, 0, 1, 0, 1])

    # WHEN
    sudoku = Sudoku(sample_sudoku)
    nonzero = NonzeroNumbers(sudoku)
    columns = nonzero.columns

    # THEN
    assert np.all(columns == expected_columns)


def test_numbers_property_works_properly():
    # GIVEN
    sample_sudoku = np.array([[0, 1], [0, 0], [2, 2], [3, 7]])
    expected_numbers = np.array([0, 1, 1, 2, 6])

    # WHEN
    sudoku = Sudoku(sample_sudoku)
    nonzero = NonzeroNumbers(sudoku)
    numbers = nonzero.numbers

    # THEN
    assert np.all(numbers == expected_numbers)
