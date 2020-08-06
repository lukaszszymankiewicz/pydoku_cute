from numpy import load

UNSOLVED_SUDOKU_PATH = "src/static/unsolved/sample_"


def load_sample_unsolved_sudoku(number: int):
    try:
        return load(UNSOLVED_SUDOKU_PATH + str(number) + ".npy")
    except FileNotFoundError:
        raise FileNotFoundError("sample of sudoku you are looking for cannot be found")
