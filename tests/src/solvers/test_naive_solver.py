import pytest

from src.static.file_loaders import load_sample_unsolved_sudoku
from src.solvers.naive_solver import naive_solver
from src.objects.sudoku import Sudoku


@pytest.mark.parametrize("probe", list(range(101)))
def test_naive_solver_works_for_simples_cases(probe):
    # GIVEN
    sudoku = Sudoku(load_sample_unsolved_sudoku(probe))

    # WHEN
    solved_sudoku = naive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
