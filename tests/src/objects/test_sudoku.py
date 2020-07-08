import numpy as np

from src.objects import Sudoku


def test_is_not_solved_sudoku_works_properly():
    # GIVEN
    sample_solved_sudoku_array = np.array([[1, 2], [1, 2]])
    sample_not_solved_sudoku_array = np.array([[0, 2], [0, 2]])

    sample_solved_sudoku = Sudoku(sample_solved_sudoku_array)
    sample_not_solved_sudoku = Sudoku(sample_not_solved_sudoku_array)

    # THEN
    assert sample_solved_sudoku.is_not_solved == False
    assert sample_not_solved_sudoku.is_not_solved == True

def test_initializing_empty_sudoku_returns_proper_sudoku():
    pass

def test_initalizing_not_empty_sudoku_return_proper_sudoku():
    pass

def test_update_nonzeros_function_returns_proper_results():
    pass
