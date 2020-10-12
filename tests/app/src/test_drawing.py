from os import remove
from pathlib import Path

import numpy as np
import pytest
from app.src.drawing import convert_array_to_png_image, draw_sudoku
from app.src.file_loaders import load_sample_unsolved_sudoku
from app.src.sudoku import Sudoku


@pytest.mark.parametrize("probe", list(range(100)))
def test_draw_sudoku_works_properly_for_nonsolved_sudokus(probe):
    # GIVEN
    sample_path = f"./tests/app/images/sample_{probe}.png"
    sudoku = Sudoku(load_sample_unsolved_sudoku(probe))
    expected_suffix = ".png"

    # WHEN
    draw_sudoku(sudoku=sudoku, path=sample_path)

    # THEN
    assert Path(sample_path).suffix == expected_suffix

    # cleaning up!
    remove(sample_path)


def test_convert_array_to_png_image_works_anyhow():
    # GIVEN
    sample_matrix = np.ones((100, 100)).astype(np.int8)
    sample_path = f"./tests/app/images/sample_42.png"
    expected_suffix = ".png"

    # WHEN
    convert_array_to_png_image(matrix=sample_matrix, file_path=sample_path)

    # THEN
    assert Path(sample_path).suffix == expected_suffix

    # cleaning up!
    remove(sample_path)
