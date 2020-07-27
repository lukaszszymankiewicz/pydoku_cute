import pytest

import numpy as np

from src.generators.naive_generator import naive_generator
from src.static.constants import SQUARES


@pytest.mark.parametrize("n_cells", list(range(81)))
def test_naive_generator_return_proper_number_of_empty_cells(n_cells):
    # GIVEN
    expected_number_of_filled_cells = 9*9-n_cells

    # WHEN
    generated_sudoku = naive_generator(n_cells)
    number_of_filled_cells = np.count_nonzero(generated_sudoku)

    # THEN
    assert expected_number_of_filled_cells == number_of_filled_cells


@pytest.mark.parametrize("n_cells", list(range(81)))
def test_naive_generator_returns_unique_values_in_rows(n_cells):
    """
    To check if values in array (row) are unique they are first sorted, and then a diff between
    all values are calculated. If diff between aby two values are equal to zero, means that they
    are in fact the same number.
    """
    # GIVEN
    expected_number_of_filled_cells = 9*9-n_cells

    # WHEN & THEN
    generated_sudoku = naive_generator(n_cells)

    for row in generated_sudoku:
        row.sort()
        row_with_cleaned_zeros = row[row != 0]

        if len(row_with_cleaned_zeros) == 0:
            # if len of row after cutting all zeros is empty, there is nothing to assert
            pass
        else:
            diff = np.diff(row_with_cleaned_zeros)
            assert np.all(diff != 0)


@pytest.mark.parametrize("n_cells", list(range(81)))
def test_naive_generator_returns_unique_values_in_columns(n_cells):
    """
    To check if values in array (column) are unique they are first sorted, and then a diff between
    all values are calculated. If diff between aby two values are equal to zero, means that they
    are in fact the same number.
    """
    # GIVEN
    expected_number_of_filled_cells = 9*9-n_cells

    # WHEN & THEN
    generated_sudoku = naive_generator(n_cells)

    for col in generated_sudoku.T:
        col.sort()
        col_with_cleaned_zeros = col[col != 0]

        if len(col_with_cleaned_zeros) == 0:
            # if len of row after cutting all zeros is empty, there is nothing to assert
            pass
        else:
            diff = np.diff(col_with_cleaned_zeros)
            assert np.all(diff != 0)


@pytest.mark.parametrize("n_cells", list(range(81)))
def test_naive_generator_returns_unique_values_in_squares(n_cells):
    """
    To check if values in array (column) are unique they are first sorted, and then a diff between
    all values are calculated. If diff between aby two values are equal to zero, means that they
    are in fact the same number.
    """
    # GIVEN
    expected_number_of_filled_cells = 9*9-n_cells

    # WHEN & THEN
    generated_sudoku = naive_generator(n_cells)

    for square in SQUARES:
        square_values = generated_sudoku[square[0], square[1]]
        square_values = square_values.flatten()
        square_values.sort()
        square_with_cleaned_zeros = square_values[square_values != 0]

        if len(square_with_cleaned_zeros) == 0:
            # if len of row after cutting all zeros is empty, there is nothing to assert
            pass
        else:
            diff = np.diff(square_with_cleaned_zeros)
            assert np.all(diff != 0)
