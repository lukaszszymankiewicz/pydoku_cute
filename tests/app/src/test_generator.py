import numpy as np
import pytest
from app.src.enums import Difficult
from app.src.generator import generate


@pytest.mark.parametrize("difficult", Difficult.legal_difficulties)
def test_generate_function_works_properly_for_all_given_difficulties(difficult):
    # WHEN
    solved_sudoku, unsolved_sudoku = generate(difficult=difficult)

    # THEN
    assert np.any(solved_sudoku.array == 0)
    assert not np.any(unsolved_sudoku.array == 0)
