import numpy as np

from src.file_loaders.load_sample_sudoku import load_sample_solved_sudoku

from src.objects.utils.random import (
    generate_random_indices_of_nonzero_elements,
    generate_numbers_mapping,
    generate_random_order_of_groups,
    generate_random_order,
    generate_bool,
)
from src.objects.utils.misc import replace_values


def naive_generator(n_empty_cells = 45) -> np.ndarray:
    sudoku = load_sample_solved_sudoku(np.random.randint(100))

    # generate all random order
    mapping = generate_numbers_mapping()
    random_rows_order = generate_random_order()
    random_columns_order = generate_random_order()
    random_groups_of_rows_order = generate_random_order_of_groups()
    random_groups_of_columns_order = generate_random_order_of_groups()
    flip_vertically = generate_bool()
    flip_horizontally = generate_bool()

    # using above random order shuffle the sudoku
    sudoku = replace_values(sudoku, mapping)
    sudoku = sudoku[:, random_columns_order]
    sudoku = sudoku[random_rows_order, :]
    sudoku = sudoku[random_groups_of_rows_order, :]
    sudoku = sudoku[:, random_columns_order]

    if flip_vertically:
        sudoku = np.flipud(sudoku)

    if flip_horizontally:
        sudoku = np.fliplr(sudoku)

    # having full random solved sudoku, set some cells to empty
    random_nonzero_value = generate_random_indices_of_nonzero_elements(sudoku, n_empty_cells)
    sudoku[random_nonzero_value[0], random_nonzero_value[1]] = 0

    return sudoku
