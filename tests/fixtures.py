import numpy as np
import pytest


@pytest.fixture
def sample_sudoku_3x3():
    return np.array(
        [
            [7, 2, 0, 0, 0, 6, 1, 0, 0,],
            [6, 0, 0, 0, 1, 0, 0, 0, 4,],
            [8, 0, 9, 0, 0, 3, 0, 0, 5,],
            [0, 0, 0, 0, 4, 0, 0, 0, 0,],
            [0, 0, 0, 8, 5, 2, 0, 0, 7,],
            [0, 5, 0, 0, 0, 0, 9, 0, 0,],
            [0, 0, 0, 0, 0, 0, 5, 0, 3,],
            [2, 0, 0, 6, 3, 0, 4, 0, 0,],
            [0, 0, 0, 2, 0, 0, 0, 7, 9,],
        ]
    )


@pytest.fixture
def sample_sudoku_2x2():
    return np.array([[2, 0, 0, 1], [0, 4, 3, 0], [0, 2, 1, 0], [3, 0, 0, 4],])
