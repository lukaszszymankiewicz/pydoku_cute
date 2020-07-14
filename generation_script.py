import numpy as np

from src.generators.recursive_generator import recursive_conclusive_generator
from src.solvers.naive_solver import naive_solver


for i in range(99, 101):

    sudoku = recursive_conclusive_generator()
    solved = naive_solver(sudoku).sudoku.array
    with open("./src/static/solved/sample_" + str(i) + ".npy", "wb") as file:
        np.save(file, sudoku)
