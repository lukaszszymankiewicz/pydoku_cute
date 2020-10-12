import numpy as np
import pytest
from app.src.file_loaders import (
    load_empty_frame,
    load_number,
    load_numbers_pallete,
    load_sample_unsolved_sudoku,
)


def test_empty_frame_returns_proper_numpy_array():
    # GIVEN
    expected_type = np.ndarray
    expected_dtype = np.uint8
    expected_shape = (938, 938)

    # WHEN
    frame = load_empty_frame()

    # THEN
    assert type(frame) == expected_type
    assert frame.dtype == expected_dtype
    assert frame.shape == expected_shape


def test_load_numbers_pallete_return_numpy_archive_with_every_number():
    # GIVEN
    expected_shape = (100, 100)
    expected_type = np.ndarray
    expected_dtype = np.uint8
    exected_numbers = ["number_" + str(number) for number in range(1, 10)]

    # WHEN
    numbers_pallete = load_numbers_pallete()

    # THEN
    for expected_number in exected_numbers:
        assert numbers_pallete[expected_number].shape == expected_shape
        assert numbers_pallete[expected_number].dtype == expected_dtype
        assert type(numbers_pallete[expected_number]) == expected_type


@pytest.mark.parametrize("number", list(range(0, 9)))
def test_load_number_loads_all_number_properly(number):
    # GIVEN
    expected_shape = (100, 100)
    expected_type = np.ndarray
    expected_dtype = np.uint8
    numbers_pallete = load_numbers_pallete()

    # WHEN
    loaded_number_image = load_number(numbers_pallete, number)

    # THEN
    assert loaded_number_image.shape == expected_shape
    assert loaded_number_image.dtype == expected_dtype
    assert type(loaded_number_image) == expected_type


@pytest.mark.parametrize("wrong_number", [-1, 10])
def test_load_number_raises_attribute_error_if_number_within_range_is_inputted(wrong_number):
    # GIVEN
    numbers_pallete = load_numbers_pallete()

    # WHEN & THEN
    with pytest.raises(AttributeError):
        load_number(numbers_pallete, wrong_number)


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
