import numpy as np

from objects.utils.misc import replace_values


def test_replace_values_works_properly():
    # GIVEN
    sample_array = np.array([1,2,3,4])
    sample_map = {1:2, 2:3, 3:4, 4:5}
    expected_array = np.array([2,3,4,5])

    # WHEN
    array_after_replacing = replace_value(sample_array, sample_map)

    # THEN
    assert np.all(array_after_replacing == expected_array) 
    assert array_after_replacing.shape == expected_array.shape
