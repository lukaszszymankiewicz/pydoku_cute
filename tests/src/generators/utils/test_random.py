from numpy import array, hstack, all, vstack
import pytest
from src.generators.utils.random import get_random_indices


def test_get_random_indices_works_properly_for_sample_size_equqal_to_one():
    # GIVEN
    sample_matrix = array([[1, 2], [3, 4]])

    # WHEN
    random_indices = get_random_indices(matrix=sample_matrix, sample_size=1)
    random_indices = hstack(random_indices)

    # THEN
    assert all(random_indices == sample_matrix[0]) or all(random_indices == sample_matrix[1])
