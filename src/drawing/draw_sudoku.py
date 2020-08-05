from src.objects.sudoku import Sudoku
from src.static.file_loaders import load_numbers_pallete, load_number, load_empty_frame
from src.drawing.utils import calculate_image_place, convert_array_to_png_image


def draw_sudoku(sudoku: Sudoku, path:str):
    frame = load_empty_frame()
    numbers_pallete = load_numbers_pallete()

    indices = sudoku.where_is_filled
    numbers = sudoku.filled_numbers

    for (row, col), number in zip(indices, numbers):
        number_array = load_number(numbers_pallete, number)
        number_position = calculate_image_place(row, col)
        frame[number_position] = number_array

    return convert_array_to_png_image(frame, path)
