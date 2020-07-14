import numpy as np


def replace_values(array:np.ndarray, mapping:dict):
    result = np.ones_like(array)
    for old_value, new_value in mapping.items():
        result[array == old_value] = new_value
    return result


def find_unique_number(array:np.ndarray, axis:int) -> np.ndarray:
    mask = (array != 0).sum(axis=axis, keepdims=True) > 1
    # TODO: add generit type
    candidates = np.where(mask, 0, array).astype(np.uint8)
    candidates_indices = np.nonzero(candidates)

    return candidates_indices

