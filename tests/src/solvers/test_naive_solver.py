import pytest

import numpy as np

from src.generators.naive_generator import naive_generate
from src.static.samples import sample1, sample2, sample3, sample4
from src.solvers.naive_solver import naive_solver


@pytest.mark.parametrize("sample", [(sample1), (sample2), (sample3), (sample4)])
def test_solve_function_works_for_3x3_sudoku(sample):
    # WHEN
    solved_sudoku = solve(sample)

    # THEN
    all_numbers_are_present_in_rows(solved_sudoku)
    all_numbers_are_present_in_columns(solved_sudoku)
    all_numbers_are_present_in_every_square(solved_sudoku)

def testx_xxx_solve_function_works_for_generated_2x2_sudoku():
    # WHEN
    sudoku = generate(digits_num=10, size=4)

    # THEN
    breakpoint()
    solved_sudoku = solve(sudoku)
    breakpoint()

    all_numbers_are_present_in_rows(solved_sudoku)
    all_numbers_are_present_in_columns(solved_sudoku)
    all_numbers_are_present_in_every_square(solved_sudoku)

def all_numbers_are_present_in_rows(array: np.ndarray):
    size = array.shape[0]
    available_numbers = np.arange(1, size + 1)
    sorted_array = np.sort(array, axis=1)
    assert np.all(sorted_array == available_numbers)


def all_numbers_are_present_in_columns(array: np.ndarray):
    size = array.shape[0]
    available_numbers = np.arange(1, size + 1).reshape(-1, 1)
    sorted_array = np.sort(array, axis=0)
    assert np.all(sorted_array == available_numbers)


def all_numbers_are_present_in_every_square(array: np.ndarray):
    size = array.shape[0]
    square_size = np.sqrt(size).astype(int)

    squares_in_row = np.arange(square_size)
    squares_in_cols = np.arange(square_size)

    available_numbers = np.arange(1, size + 1)

    for square_row in squares_in_row:
        for square_col in squares_in_cols:
            row_start_index = square_row // square_size * square_size
            row_end_index = row_start_index + square_size

            col_start_index = square_col // square_size * square_size
            col_end_index = col_start_index + square_size

            square_vals = array[row_start_index:row_end_index, col_start_index:col_end_index]
            square_vals_sorted = np.sort(square_vals.flatten())

            assert np.all(square_vals_sorted == available_numbers)
