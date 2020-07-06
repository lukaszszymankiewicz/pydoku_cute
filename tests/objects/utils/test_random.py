import numpy as np

from objects.utils.random import (
    get_random_nonzero_elements_of_array,
    generate_numbers_mapping,
    generate_random_order,
    generate_random_order_of_groups,
    )

def test_get_random_nonzero_elements_of_array_return_proper_number_of_elements():
    # GIVEN
    sample_n_elements = 3
    sample_array = np.array([[1,2,3,4,0,0,0,8,9]])
    number_of_rows = sample_array.shape[0]
    expected_shape = (number_of_rows, sample_n_elements)

    # WHEN
    random_nonzero_elements = get_random_nonzero_elements_of_array(sample_array, sample_n_elements)

    # THEN
    assert random_nonzero_elements.shape == expected_shape


def test_get_random_nonzero_elements_of_array_return_proper_numbers():
    # GIVEN
    sample_n_elements = 6
    sample_array = np.array([[1,2,3,4,0,0,0,8,9]])
    expected_result = np.array([[1,2,3,4,8,9]])

    # WHEN
    random_nonzero_elements = get_random_nonzero_elements_of_array(sample_array, sample_n_elements)

    # THEN
    assert expected_result == random_nonzero_elements 


def test_generate_numbers_mapping_return_dict_with_proper_keys_and_values():
    # GIVEN
    expected_sorted_keys = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    expected_sorted_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # WHEN
    resulted_mapping =  generate_numbers_mapping()
    resulted_keys = np.array(list(resulted_mapping.keys()))
    resulted_values = np.array(list(resulted_mapping.values()))
    resulted_keys.sort()
    resulted_values.sort()

    # THEN
    assert np.all(expected_sorted_keys == resulted_keys)
    assert np.all(expected_sorted_values == resulted_values)


def test_generate_random_order_returns_proper_results():
    # GIVEN
    expected_results_in_first_group = np.array([0,1,2])
    expected_results_in_second_group = np.array([3,4,5])
    expected_results_in_third_group = np.array([6,7,8])

    # WHEN
    random_order = generate_random_order()

    first_group = random_order[0:2]
    second_irst_group = random_order[3:5]
    third_group = random_order[6:8]

    first_group.sort()
    second_group.sort()
    third_group.sort()

    # THEN
    assert np.all(first_group == expected_results_in_first_group)
    assert np.all(second_group == expected_results_in_second_group)
    assert np.all(third_group == expected_results_in_third_group)


def test_generate_random_order_of_groups_return_proper_results():
    # GIVEN
    expected_sorted_results = np.array([1,2,3,4,5,6,7,8])

    # WHEN
    random_order_of_groups = generate_random_order_of_groups()
    random_order_of_groups.sort()

    # THEN
    assert np.all(expected_sorted_results == random_order_of_groups)
