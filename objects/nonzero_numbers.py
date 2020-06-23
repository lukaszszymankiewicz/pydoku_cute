import numpy as np


class NonzeroNumbers:
    def __init__(self, sudoku):
        self.indices = np.nonzero(sudoku.array)
        self.nonzero_numbers = sudoku.array[self.indices] - 1
        self.square_size = np.sqrt(sudoku.array.shape[0]).astype(int)

    @property
    def numbers(self):
        return self.nonzero_numbers
