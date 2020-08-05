import numpy as np

from src.static.file_loaders import load_empty_frame


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
