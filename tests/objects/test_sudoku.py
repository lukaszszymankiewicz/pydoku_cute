import numpy as np
from pydoku.objects import Sudoku


def test_is_not_solved_sudoku_works_properly():
    # GIVEN
    sample_solved_sudoku_array = np.array([[1, 2], [1, 2]])
    sample_not_solved_sudoku_array = np.array([[0, 2], [0, 2]])

    sample_solved_sudoku = Sudoku(sample_solved_sudoku_array)
    sample_not_solved_sudoku = Sudoku(sample_not_solved_sudoku_array)

    # THEN
    assert sample_solved_sudoku.is_not_solved == False
    assert sample_not_solved_sudoku.is_not_solved == True


def test_add_function_works_properly():
    # GIVEN
    sample_sudoku_array = np.array([[1, 2], [0, 0]])
    sample_numbers_to_add = np.array([[1, 0], [1, 0]])
    expected_sudoku_array_after_adding = np.array([[1, 2], [1, 0]])

    # WHEN
    sample_sudoku = Sudoku(sample_sudoku_array)
    sample_sudoku.add_numbers(sample_numbers_to_add)
    sudoku_array_after_adding = sample_sudoku.array

    # THEN
    assert np.all(sudoku_array_after_adding == expected_sudoku_array_after_adding)
