import numpy as np
import pytest
from app.src.enums import Difficult
from app.src.file_loaders import load_sample_unsolved_sudoku
from app.src.generator import generate
from app.src.naive_solver import naive_solver
from app.src.sudoku import Sudoku
from tests.conftest import sudoku_is_valid


@pytest.mark.parametrize("probe", list(range(100)))
def test_naive_solver_works_for_generated_cases(probe):
    # GIVEN
    sudoku, _ = generate(Difficult.easy)

    # WHEN
    solved_sudoku = naive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True


@pytest.mark.parametrize("probe", list(range(10)))
@pytest.mark.parametrize("difficult", ["medium", "hard", "impossible"])
def test_naive_solver_returns_unfilled_sudoku_if_it_cannot_solved_puzzle(probe, difficult):
    # GIVEN
    sudoku, _ = generate(difficult)

    # WHEN
    solved_sudoku = naive_solver(sudoku)

    # THEN
    assert isinstance(sudoku, Sudoku)


@pytest.mark.parametrize("probe", list(range(100)))
def test_naive_solver_works_for_simple_cases(probe):
    # GIVEN
    sudoku = Sudoku(load_sample_unsolved_sudoku(probe))

    # WHEN
    solved_sudoku = naive_solver(sudoku)

    # THEN
    assert solved_sudoku.is_solved == True
    assert sudoku_is_valid(solved_sudoku.array) == True
