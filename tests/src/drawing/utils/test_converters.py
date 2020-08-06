from os import remove
from pathlib import Path

from numpy import uint8, zeros

from src.drawing.utils.converters import convert_array_to_png_image


def test_convert_array_to_png_image_works_properly():
    # GIVEN
    sample_array = zeros((100, 100), dtype=uint8)
    sample_path = "./tests/src/drawing/utils/sample.png"
    expected_suffix = ".png"

    # WHEN
    convert_array_to_png_image(sample_array, sample_path)

    # THEN
    assert Path(sample_path).suffix == expected_suffix

    # cleaning up!
    remove(sample_path)
