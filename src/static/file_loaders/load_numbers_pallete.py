from numpy import load

NUMBERS_PALLETE_PATH = "src/static/images/numbers_pallete.npz"


def load_numbers_pallete():
    return load(NUMBERS_PALLETE_PATH)
