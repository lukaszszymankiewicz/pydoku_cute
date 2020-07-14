import numpy as np

from src.objects import Sudoku
from src.static.full_board import full_board
from src.objects.utils.constants import SQUARES


def test_is_not_solved_sudoku_works_properly():
    # GIVEN
    sample_solved_sudoku_array = np.array([[1, 2], [1, 2]])
    sample_not_solved_sudoku_array = np.array([[0, 2], [0, 2]])

    sample_solved_sudoku = Sudoku(sample_solved_sudoku_array)
    sample_not_solved_sudoku = Sudoku(sample_not_solved_sudoku_array)

    # THEN
    assert sample_solved_sudoku.is_solved == True
    assert sample_not_solved_sudoku.is_solved == False


def test_initializing_empty_sudoku_returns_proper_sudoku():
    # GIVEN
    expected_empty_sudoku_array = np.zeros((9, 9)).astype(np.uint8)

    # WHEN
    empty_sudoku_array = Sudoku().array

    # THEN
    assert np.all(expected_empty_sudoku_array == empty_sudoku_array)


def test_initalizing_not_empty_sudoku_return_proper_sudoku():
    # GIVEN
    sample_sudoku_values = np.zeros((9,9)).astype(np.uint8)
    sample_sudoku_values[0, 0] = 9
    
    # WHEN
    sudoku = Sudoku(sample_sudoku_values)
    
    # THEN
    assert np.all(sudoku.array == sample_sudoku_values)


def test_update_nonzeros_function_returns_proper_results():
    # GIVEN
    expected_nonzero_object_values = (np.array([0]), np.array([0]))
    expected_nonzero_numbers = np.array([2])
    sudoku = Sudoku()

    # WHEN
    sudoku.array[0,0] = 3
    sudoku.update_nonzeros()

    # THEN
    assert np.all(sudoku._nonzeros.indices == expected_nonzero_object_values)
    assert np.all(sudoku._nonzeros.nonzero_numbers == expected_nonzero_numbers)


def test_add_numbers_function_works_properly():
    # GIVEN
    values_to_fill = (np.array([0,8]), np.array([1,6]), np.array([5,2]))

    expected_sudoku_array = np.zeros((9,9)).astype(np.uint8)
    expected_sudoku_array[0,1] = 6
    expected_sudoku_array[8,6] = 3

    # WHEN
    sudoku = Sudoku()
    sudoku.add_numbers(*values_to_fill)

    # THEN
    assert np.all(sudoku.array == expected_sudoku_array)


def test_find_sole_candidates_in_squares_works_properly():
    # GIVEN
    array = full_board
    expected_sole_candidates_in_squares = (np.array([0,7]), np.array([0,7]), np.array([7,4]))
    array[0, 0] = 0
    array[7, 7] = 0

    # WHEN
    sudoku = Sudoku(array)
    sudoku.update_possibilities()
    sole_candidates_in_squares = sudoku.find_sole_candidates_in_squares()

    # THEN
    for expected, candidates in zip(expected_sole_candidates_in_squares, sole_candidates_in_squares):
        assert all(expected == candidates)
