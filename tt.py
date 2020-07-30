import numpy as np
import time
from src.solvers.naive_solver import naive_solver
from src.generators.recursive_generator import recursive_conclusive_generator

times = []
for i in range(100):
    st = time.time()
    sudoku = recursive_conclusive_generator()
    np.save(f"src/static/unsolved/sample_{i}.npy", sudoku.array)
    end = time.time()
    times.append((end-st))

print(sum(times) / 100)
