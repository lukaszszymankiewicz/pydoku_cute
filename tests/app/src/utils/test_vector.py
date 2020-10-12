import numpy as np
from app.src.utils.vector import filter_zeros_from_vector


def test_filter_zeros_from_vector_works_properly():
    # GIVEN
    sample_vector = np.array([0, 1, 2, 3, 0, 5, 6, 0])
    expected_result = np.array([1, 2, 3, 5, 6])

    # WHEN
    filtered_vector = filter_zeros_from_vector(sample_vector)

    # THEN
    assert np.all(filtered_vector == expected_result)


def test_filter_zeros_from_vector_returns_empty_vector_for_zero_only_input():
    # GIVEN
    sample_vector = np.array([0, 0, 0, 0, 0, 0, 6, 0])
    expected_result = np.array([])

    # WHEN
    filtered_vector = filter_zeros_from_vector(sample_vector)

    # THEN
    assert np.all(filtered_vector == expected_result)
