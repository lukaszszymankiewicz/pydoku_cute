import numpy as np

from src.solvers.recursive_solver import recursive_solver
from src.solvers.naive_solver import naive_solver


def recursive_conclusive_generator(n_min_numbers: int = 1):
    to_place = np.arange(1, 10).astype(np.uint8)
    np.random.shuffle(to_place)
    empty_sudoku = np.zeros((9, 9)).astype(np.uint8)
    indices = np.argwhere(empty_sudoku == 0)
    random_indices = np.random.choice(a=indices.shape[0], size=9)

    for index, value in zip(random_indices, to_place):
        row = indices[index][0]
        col = indices[index][1]
        empty_sudoku[row, col] = value

    filled_sudoku = recursive_solver(empty_sudoku).sudoku.array

    while True:
        last_step_sudoku = np.copy(filled_sudoku)

        nonzeros = np.argwhere(last_step_sudoku)
        random_number = np.random.randint(low=0, high=nonzeros.shape[0])
        row = nonzeros[random_number][0]
        col = nonzeros[random_number][1]
        last_step_sudoku[row, col] = 0

        if naive_solver(last_step_sudoku).is_solved == False:
            return filled_sudoku
        else:
            filled_sudoku[row, col] = 0
