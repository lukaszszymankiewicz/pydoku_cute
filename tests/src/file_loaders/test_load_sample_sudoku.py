import pytest

import numpy as np

from src.static.file_loaders import load_sample_unsolved_sudoku


@pytest.mark.parametrize("probe", list(range(100)))
def test_load_sample_sudoku_returns_proper_array(probe):
    # GIVEN & WHEN 
    sudoku_array = load_sample_unsolved_sudoku(probe)

    # THEN
    assert type(sudoku_array) == np.ndarray


def test_load_sample_sudoku_raises_error_if_wrong_probe_is_inputted():
    # GIVEN
    wrong_probe_number = 101

    # GIVEN 
    with pytest.raises(FileNotFoundError):
        load_sample_unsolved_sudoku(wrong_probe_number)
