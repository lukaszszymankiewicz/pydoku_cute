import numpy as np


NUMBERS_PALLETE_PATH = "src/static/images/numbers_pallete.npz"


def load_numbers_pallete():
    return np.load(NUMBERS_PALLETE_PATH)
