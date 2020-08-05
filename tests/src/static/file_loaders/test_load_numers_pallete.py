import numpy as np

from src.static.file_loaders import load_numbers_pallete


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

