import numpy as np

from src.static.constants import SQUARE_NUMBERS, SUDOKU_INDICES, SUDOKU_NUMBERS


def generate_random_indices_of_nonzero_elements(array: np.ndarray, sample_size: int) -> np.ndarray:
    possibilities = np.vstack(np.nonzero(array))
    random_index = np.random.choice(a=possibilities.shape[1], size=sample_size, replace=False)
    return possibilities[:, random_index]


def generate_bool():
    return np.random.choice([True, False])


def generate_numbers_mapping():
    """
    Generates mapping of numbers used in sudoku to other same numbers but in different
    permutation. That alows us to exchange numbers while generating sudoku t solve.
    """

    keys = SUDOKU_NUMBERS
    values = SUDOKU_NUMBERS
    np.random.shuffle(values)
    return dict(zip(keys, values))


def generate_random_order():
    old_order = SUDOKU_INDICES
    groups = np.split(old_order, SQUARE_NUMBERS)
    for group in groups:
        np.random.shuffle(group)
    return np.concatenate(groups)


def generate_random_order_of_groups():
    old_order = SUDOKU_INDICES
    groups = np.split(old_order, 3)
    np.random.shuffle(groups)
    return np.concatenate(groups)
