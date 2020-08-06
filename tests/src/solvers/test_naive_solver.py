import pytest

from src.generators import generate
from src.objects.sudoku import Sudoku
from src.solvers.naive_solver import naive_solver
from src.static.file_loaders import load_sample_unsolved_sudoku
from tests.conftest import sudoku_is_valid
from src.generators.utils.enums import Difficult


@pytest.mark.parametrize("probe", list(range(100)))
def test_naive_solver_works_for_generated_cases(probe):
    # GIVEN
    sudoku, _ = generate(Difficult.easy)

    # WHEN
    solved_sudoku = naive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True


@pytest.mark.parametrize("probe", list(range(100)))
def test_naive_solver_works_for_simple_cases(probe):
    # GIVEN
    sudoku = Sudoku(load_sample_unsolved_sudoku(probe))

    # WHEN
    solved_sudoku = naive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True
