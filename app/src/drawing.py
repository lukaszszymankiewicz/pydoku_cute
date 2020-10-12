import png

from .file_loaders import load_empty_frame, load_number, load_numbers_pallete
from .sudoku import Sudoku
from .types import FilePath, Matrix
from .utils import calculate_image_place


def draw_sudoku(sudoku: Sudoku, path: FilePath) -> None:
    """Draws Sudoku objects and converts it into png file. Empty Frame image, every number image
    are loaded separatly and combined to achieve proper image.

    Attrs:
        sudoku - Sudoku object (solved or unsolved),
        path - string representing place where sudoku image will be saved.

    Returns:
        None.
    """

    frame = load_empty_frame()
    numbers_pallete = load_numbers_pallete()

    indices = sudoku.where_is_filled
    numbers = sudoku.filled_numbers

    for (row, col), number in zip(indices, numbers):
        number_image = load_number(numbers_pallete, number)
        image_place = calculate_image_place(row, col)
        frame[image_place] = number_image

    convert_array_to_png_image(frame, path)


def convert_array_to_png_image(matrix: Matrix, file_path: FilePath) -> None:
    """
    Converts inuputted 2d numpy array into .png file.

    Args:
        matrix: 2d numpy array (must be 2d, and np.uint8 dtype!),
        file_path: place where resulted png will be saved.

    Returns:
        None
    """
    png.from_array(matrix, mode="L").save(file_path)
