from typing import List

from src.static.types import Scalar, Index

from src.static.constants import (
    CELL_SIZE,
    HARD_LINE_WIDTH,
    LIGHT_LINE_WIDTH,
    MEDIUM_LINE_WIDTH,
)


def calculate_image_place(row_index: Index, col_index: Index) -> List[slice]:
    row_position = calculate_offset(row_index)
    col_position = calculate_offset(col_index)
    return (
        slice(row_position, row_position + CELL_SIZE),
        slice(col_position, col_position + CELL_SIZE),
    )


def calculate_offset(index: Index) -> Scalar:
    return calculate_image_offset_from_frame(index) + calculate_image_offset_from_cells(index)


def calculate_image_offset_from_frame(index: Index) -> Scalar:
    hard_line_offset = HARD_LINE_WIDTH
    medium_line_offset = (index // 3) * MEDIUM_LINE_WIDTH
    light_line_offset = (index - index // 3) * LIGHT_LINE_WIDTH
    return hard_line_offset + medium_line_offset + light_line_offset


def calculate_image_offset_from_cells(index: Index) -> Scalar:
    return index * CELL_SIZE
