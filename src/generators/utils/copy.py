from copy import deepcopy

from src.objects.sudoku import Sudoku


def copy_sudoku(sudoku):
    return Sudoku(array=deepcopy(sudoku.array))
