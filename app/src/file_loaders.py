import numpy as np

EMPTY_FRAME_PATH = "app/src/static/images/empty_frame.npz"
NUMBERS_PALLETE_PATH = "app/src/static/images/numbers_pallete.npz"
UNSOLVED_SUDOKU_PATH = "app/src/static/unsolved/sample_"


def load_empty_frame() -> np.ndarray:
    """Loads empty sudoku grid as a numpy array."""

    return np.load(EMPTY_FRAME_PATH)["empty_frame"]


def load_number(numbers_pallete: dict, number_to_draw: int) -> np.ndarray:
    """Chooses one image number from pallete.

    Attrs:
        number_pallete - archive containing all image numbers stored as numpy arrays,
        number_to_draw - integer number representing number to coose from pallete.

    Returns:
        numpy array representing image of chose number.

    Raises:
        AttributeError - if inputted number is not from proper range.
    """

    if number_to_draw < 0 or number_to_draw > 9:
        raise AttributeError("image of number must be from range 0 to 9!")

    return numbers_pallete["number_" + str(number_to_draw + 1)]


def load_numbers_pallete() -> np.ndarray:
    """Loads numbers pallete (archive containing all image numbers from 1 to 9)."""

    return np.load(NUMBERS_PALLETE_PATH)


def load_sample_unsolved_sudoku(number: int) -> np.ndarray:
    """Loads one sample sudoku array."""
    try:
        return np.load(UNSOLVED_SUDOKU_PATH + str(number) + ".npy")
    except FileNotFoundError:
        raise FileNotFoundError("sample of sudoku you are looking for cannot be found")
