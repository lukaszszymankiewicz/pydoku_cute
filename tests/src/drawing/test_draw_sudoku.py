import pytest

from os import remove

from pathlib import Path
from src.objects import Sudoku
from src.drawing.draw_sudoku import draw_sudoku
from src.static.file_loaders.load_sample_sudoku import load_sample_unsolved_sudoku


@pytest.mark.parametrize("probe", list(range(100)))
def test_draw_sudoku_works_properly_for_nonsolved_sudokus(probe):
    # GIVEN
    sample_path = f"./tests/src/drawing/sample_{probe}.png"
    sudoku = Sudoku(load_sample_unsolved_sudoku(probe))
    expected_suffix = ".png"

    # WHEN
    draw_sudoku(sudoku=sudoku, path=sample_path)

    # THEN
    assert Path(sample_path).suffix == expected_suffix

    # cleaning up!
    remove(sample_path)
