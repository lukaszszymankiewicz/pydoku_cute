import numpy as np


class PossiblesMatrix:
    def __init__(self, sudoku):
        self.side = sudoku.shape[0]
        self.square_size = np.sqrt(self.side).astype(int)
        self.array = np.mgrid[1: self.side + 1, 1: self.side + 1, 1: self.side + 1][2]

    def cross_out_all_numbers_from_position(self, nonzeros):
        self.array[nonzeros.rows, nonzeros.columns, :] = 0

    def cross_out_numbers_from_columns(self, nonzeros):
        self.array[nonzeros.rows, :, nonzeros.numbers] = 0

    def cross_out_numbers_from_rows(self, nonzeros):
        self.array[:, nonzeros.columns, nonzeros.numbers] = 0

    def square_indices(self, number:int):
        start = number // self.square_size * self.square_size
        stop = start + self.square_size
        return np.arange(start, stop)

    def get_square_indices(self, row:int, col:int, number:int):
        square_row_indices = self.square_indices(row)
        square_col_indices = self.square_indices(col)
        return np.ix_(square_row_indices, square_col_indices, [number])

    def cross_out_numbers_from_squares(self, nonzeros):
        for row, col, number in zip(nonzeros.rows, nonzeros.columns, nonzeros.numbers):
            self.array[self.get_square_indices(row, col, number)] = 0

    def lonely_numbers(self, axis:int):
        mask = (self.array != 0).sum(axis=axis, keepdims=True) > 1
        return np.where(mask, 0, self.array).sum(axis=2)
