from typing import List

from src.static.types import Scalar, Index

from src.static.constants import (
    CELL_SIZE,
    HARD_LINE_WIDTH,
    LIGHT_LINE_WIDTH,
    MEDIUM_LINE_WIDTH,
)


def calculate_image_place(row_index: Index, col_index: Index) -> List[slice]:
    """
    Calculates number picture position (in pixels) to fit on frame picture in right place.

    Args:
        row_index: number from 0 to 8 reresenting cell x-position on array
        col_index: number from 0 to 8 reresenting cell y-position on array
    
    Returns:
        Two slice objects showning places of four vertices of a picture to be placed on frame.
    """
    row_position = calculate_offset(row_index)
    col_position = calculate_offset(col_index)
    return (
        slice(row_position, row_position + CELL_SIZE),
        slice(col_position, col_position + CELL_SIZE),
    )


def calculate_offset(index: Index) -> Scalar:
    """
    Calculates how many pixels image of number should be moved from 0 coordinate, basing on how 
    much frames it have from its left (or up) and hum much cells it have from left (or up) side.

    Args:
        Index: number from 0 to 8 representing index of cell.

    Returns:
        Scalar number representing offest of number picture.
    """
    return calculate_image_offset_from_frame(index) + calculate_image_offset_from_cells(index)


def calculate_image_offset_from_frame(index: Index) -> Scalar:
    """
    Calculates how many pixels image of number should be moved from 0 coordinate, basing on how 
    much frames it have from its left (or up) side.

    Args:
        Index: number from 0 to 8 representing index of cell.

    Returns:
        Scalar number representing offest of number picture.
    """
    hard_line_offset = HARD_LINE_WIDTH
    medium_line_offset = (index // 3) * MEDIUM_LINE_WIDTH
    light_line_offset = (index - index // 3) * LIGHT_LINE_WIDTH
    return hard_line_offset + medium_line_offset + light_line_offset


def calculate_image_offset_from_cells(index: Index) -> Scalar:
    """
    Calculates how many pixels image of number should be moved from 0 coordinate, basing on how
    much empty cell it have from its left (or up) side.

    Args:
        Index: number from 0 to 9 representing index of cell.

    Returns:
        Scalar number representing offest of number picture.
    """
    return index * CELL_SIZE
