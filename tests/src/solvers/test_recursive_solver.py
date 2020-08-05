import pytest

from src.generators import generate
from src.generators.utils import Difficult
from src.objects.sudoku import Sudoku
from src.solvers.recursive_solver import recursive_solver
from src.static.file_loaders import load_sample_unsolved_sudoku
from tests.conftest import sudoku_is_valid


@pytest.mark.parametrize("probe", list(range(100)))
def test_recursive_solver_works_for_simples_cases(probe):
    # GIVEN
    sudoku = Sudoku(load_sample_unsolved_sudoku(probe))

    # WHEN
    solved_sudoku = recursive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True


@pytest.mark.parametrize("probe", list(range(25)))
def test_recursive_solver_works_for_generated_easy_cases(probe):
    # GIVEN
    sudoku = generate(Difficult.easy)

    # WHEN
    solved_sudoku = recursive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True


@pytest.mark.parametrize("probe", list(range(25)))
def test_recursive_solver_works_for_generated_medium_cases(probe):
    # GIVEN
    sudoku = generate(Difficult.medium)

    # WHEN
    solved_sudoku = recursive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True


@pytest.mark.parametrize("probe", list(range(25)))
def test_recursive_solver_works_for_generated_hard_cases(probe):
    # GIVEN
    sudoku = generate(Difficult.hard)

    # WHEN
    solved_sudoku = recursive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True


@pytest.mark.parametrize("probe", list(range(25)))
def test_recursive_solver_works_for_generated_impossible_cases(probe):
    # GIVEN
    sudoku = generate(Difficult.impossible)

    # WHEN
    solved_sudoku = recursive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True
