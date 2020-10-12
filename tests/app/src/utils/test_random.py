import numpy as np
import pytest
from app.src.utils import generate_bool
from app.src.utils.random import get_random_indices


@pytest.mark.parametrize("probe", list(range(10)))
def test_generate_bool_returns_proper_results(probe):
    # GIVEN
    expected_results_pool = [True, False]

    # WHEN
    result = generate_bool()

    # THEN
    assert result in expected_results_pool
    assert type(result) == np.bool_


def test_get_random_indices_works_properly_for_sample_size_equqal_to_one():
    # GIVEN
    sample_matrix = np.array([[1, 2], [3, 4]])

    # WHEN
    random_indices = get_random_indices(matrix=sample_matrix, sample_size=1)
    random_indices = np.hstack(random_indices)

    # THEN
    assert np.all(random_indices == sample_matrix[0]) or np.all(random_indices == sample_matrix[1])
