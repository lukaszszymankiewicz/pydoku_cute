import numpy as np

from objects.static.full_board import full_board
from objects.utils.random import (
    get_random_nonzero_elements_of_array,
    generate_numbers_mapping,
    generate_random_order_of_groups,
    generate_random_order,
)
from objects.utils.misc import replace_values


def generate(n_empty_cells = 45) -> np.ndarray:
    sudoku = full_board

    # generate all random order
    mapping = generate_numbers_mapping() 
    random_rows_order = generate_random_order()
    random_columns_order = generate_random_order()
    random_groups_of_rows_order = generate_random_order_of_groups()
    random_groups_of_columns_order = generate_random_order_of_groups()

    # using above random order shuffle the sudoku
    sudoku = replace_values(sudoku, mapping)    
    sudoku = sudoku[:, random_columns_order]
    sudoku = sudoku[random_rows_order, :]
    sudoku = sudoku[random_groups_of_rows_order, :]
    sudoku = sudoku[:, random_columns_order]
    
    # having full random solved sudoku, set some cells to empty
    random_nonzero_value = get_random_nonzero_elements_of_array(sudoku, n_empty_cells)
    sudoku[random_nonzero_value[0], random_nonzero_value[1]] = 0

    return sudoku
