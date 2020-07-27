import numpy as np

EMPTY = 0
ALL = slice(None, None)

NUMBERS_TYPE = np.uint8
SIDE_SIZE = 9
SUDOKU_SIZE = (9, 9)
SQUARE_NUMBERS = 3
SUDOKU_NUMBERS = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).astype(NUMBERS_TYPE)
SUDOKU_INDICES = SUDOKU_NUMBERS - 1

SQUARE_MAPPING = {
    0: slice(0, 3, None),
    1: slice(0, 3, None),
    2: slice(0, 3, None),
    3: slice(3, 6, None),
    4: slice(3, 6, None),
    5: slice(3, 6, None),
    6: slice(6, 9, None),
    7: slice(6, 9, None),
    8: slice(6, 9, None),
}

SQUARES = [
    (slice(0, 3, None), slice(0, 3, None)),
    (slice(0, 3, None), slice(3, 6, None)),
    (slice(0, 3, None), slice(6, 9, None)),
    (slice(3, 6, None), slice(0, 3, None)),
    (slice(3, 6, None), slice(3, 6, None)),
    (slice(3, 6, None), slice(6, 9, None)),
    (slice(6, 9, None), slice(0, 3, None)),
    (slice(6, 9, None), slice(3, 6, None)),
    (slice(6, 9, None), slice(6, 9, None)),
]
