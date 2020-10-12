import numpy as np

# types
NUMBERS_TYPE = np.uint8

# constants
EMPTY = 0
SIDE_SIZE = 9
SUDOKU_SIZE = (9, 9)
SQUARE_NUMBERS = 3
SUDOKU_NUMBERS = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).astype(NUMBERS_TYPE)
SUDOKU_INDICES = SUDOKU_NUMBERS - 1

# indices
ALL = slice(None, None)
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

# images
CELL_SIZE = 100
HARD_LINE_WIDTH = 8
MEDIUM_LINE_WIDTH = 5
LIGHT_LINE_WIDTH = 2
FRAME_SIZE = [2 * HARD_LINE_WIDTH + 2 * MEDIUM_LINE_WIDTH + 6 * LIGHT_LINE_WIDTH + 9 * CELL_SIZE]
