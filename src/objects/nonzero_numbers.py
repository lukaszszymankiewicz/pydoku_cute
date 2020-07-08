import numpy as np


class NonzeroNumbers:
    def __init__(self, array):
        self.indices = np.nonzero(array)
        self.nonzero_numbers = array[self.indices] - 1

    @property
    def numbers(self):
        return self.nonzero_numbers

    @property
    def rows(self):
        return self.indices[0]

    @property
    def columns(self):
        return self.indices[1]