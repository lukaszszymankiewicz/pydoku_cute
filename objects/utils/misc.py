import numpy as np


def replace_values(array:np.ndarray, mapping:dict):
    result = np.ones_like(array)
    for old_value, new_value in mapping.items():
        result[array == old_value] = new_value
    return result
