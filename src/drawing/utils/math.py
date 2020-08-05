from src.static.constants import MEDIUM_LINE_WIDTH, HARD_LINE_WIDTH, LIGHT_LINE_WIDTH, CELL_SIZE


def calculate_image_place(row_index: int, col_index: int) -> list:
    row_position = calculate_offset(row_index)
    col_position = calculate_offset(col_index)
    return slice(row_position, row_position + CELL_SIZE), slice(col_position, col_position + CELL_SIZE)


def calculate_offset(index: int) -> int:
    return calculate_image_offset_from_frame(index) + calculate_image_offset_from_cells(index)


def calculate_image_offset_from_frame(index: int) -> int:
    hard_line_offset = HARD_LINE_WIDTH
    medium_line_offset = (index//3) * MEDIUM_LINE_WIDTH
    light_line_offset = (index - index//3) * LIGHT_LINE_WIDTH
    return hard_line_offset + medium_line_offset + light_line_offset


def calculate_image_offset_from_cells(index: int) -> int:
    return index * CELL_SIZE
