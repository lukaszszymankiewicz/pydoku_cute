import glob
import os
import uuid
from typing import Tuple

from .file_paths import (IMAGE_EXTENSION, SOLVED_SUDOKU_PREFIX,
                         SUDOKUS_FILE_PATH, UNSOLVED_SUDOKU_PREFIX)


def generate_sudokus_filenames() -> Tuple[str, str]:
    """Generates two sudoku filenames (one for solved one other for unsolved puzzle) with random
    uuid string as a interfix. These file names directs to proper folder, where images are stored.

    Args:
        None

    Returns:
        Two filepaths
    """
    random_string = str(uuid.uuid4())

    solved_sudoku = SUDOKUS_FILE_PATH + SOLVED_SUDOKU_PREFIX + IMAGE_EXTENSION
    unsolved_sudoku = SUDOKUS_FILE_PATH + UNSOLVED_SUDOKU_PREFIX + IMAGE_EXTENSION

    return solved_sudoku, unsolved_sudoku


def delete_unused_sudokus() -> None:
    """Deletes all sudokus generated before (for cleaning purposes)."""

    files = glob.glob(SUDOKUS_FILE_PATH + SOLVED_SUDOKU_PREFIX)
    for file in files:
        os.remove(file)

    files = glob.glob(SUDOKUS_FILE_PATH + UNSOLVED_SUDOKU_PREFIX)
    for file in files:
        os.remove(file)
