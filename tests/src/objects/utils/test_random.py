import numpy as np
import pytest

from src.objects.utils import generate_bool


@pytest.mark.parametrize("probe", list(range(10)))
def test_generate_bool_returns_proper_results(probe):
    # GIVEN
    expected_results_pool = [True, False]

    # WHEN
    result = generate_bool()

    # THEN
    assert result in expected_results_pool
    assert type(result) == np.bool_
