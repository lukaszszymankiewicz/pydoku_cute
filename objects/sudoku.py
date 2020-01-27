import numpy as np

class Sudoku:
    def __init__(self, array: np.array):
        self.array = array

    @property
    def is_not_solved(self):
        return 0 in self.array

    def add_numbers(self, numbers: np.array):
        self.array |= numbers
