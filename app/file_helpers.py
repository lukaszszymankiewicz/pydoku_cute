import glob
import os

from .file_paths import (APP_PREFIX, SOLVED_SUDOKU_PREFIX, SUDOKUS_FILE_PATH,
                         UNSOLVED_SUDOKU_PREFIX)


def delete_unused_sudokus() -> None:
    """Deletes all sudokus generated before (for cleaning purposes)."""

    files = glob.glob(APP_PREFIX + SUDOKUS_FILE_PATH + SOLVED_SUDOKU_PREFIX + "*")
    for file in files:
        os.remove(file)

    files = glob.glob(APP_PREFIX + SUDOKUS_FILE_PATH + UNSOLVED_SUDOKU_PREFIX + "*")
    for file in files:
        os.remove(file)
