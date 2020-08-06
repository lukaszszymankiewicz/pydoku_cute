import pytest

from src.drawing.utils.math import (
    calculate_image_offset_from_cells,
    calculate_image_offset_from_frame,
    calculate_image_place,
    calculate_offset,
)


@pytest.mark.parametrize(
    "index,expected_offset",
    [(0, 0), (1, 100), (2, 200), (3, 300), (4, 400), (5, 500), (6, 600), (7, 700), (8, 800),],
)
def test_calculate_image_offset_from_cells_works_properly(index, expected_offset):
    # WHEN
    offset = calculate_image_offset_from_cells(index)

    # THEN
    assert expected_offset == offset


@pytest.mark.parametrize(
    "index,expected_offset",
    [(0, 8), (1, 10), (2, 12), (3, 17), (4, 19), (5, 21), (6, 26), (7, 28), (8, 30),],
)
def test_calculate_image_offset_from_frame_works_properly(index, expected_offset):
    # WHEN
    offset = calculate_image_offset_from_frame(index)

    # THEN
    assert expected_offset == offset


@pytest.mark.parametrize(
    "index,expected_offset",
    [(0, 8), (1, 110), (2, 212), (3, 317), (4, 419), (5, 521), (6, 626), (7, 728), (8, 830),],
)
def test_calculate_offset_works_properly(index, expected_offset):
    # WHEN
    offset = calculate_offset(index)

    # THEN
    assert expected_offset == offset


@pytest.mark.parametrize(
    "row,col,expected_row,expected_col",
    [
        (0, 0, slice(8, 108), slice(8, 108)),
        (0, 1, slice(8, 108), slice(110, 210)),
        (0, 2, slice(8, 108), slice(212, 312)),
        (0, 3, slice(8, 108), slice(317, 417)),
        (0, 4, slice(8, 108), slice(419, 519)),
        (0, 5, slice(8, 108), slice(521, 621)),
        (0, 6, slice(8, 108), slice(626, 726)),
        (0, 7, slice(8, 108), slice(728, 828)),
        (0, 8, slice(8, 108), slice(830, 930)),
        (1, 0, slice(110, 210), slice(8, 108)),
        (1, 1, slice(110, 210), slice(110, 210)),
        (1, 2, slice(110, 210), slice(212, 312)),
        (1, 3, slice(110, 210), slice(317, 417)),
        (1, 4, slice(110, 210), slice(419, 519)),
        (1, 5, slice(110, 210), slice(521, 621)),
        (1, 6, slice(110, 210), slice(626, 726)),
        (1, 7, slice(110, 210), slice(728, 828)),
        (1, 8, slice(110, 210), slice(830, 930)),
        (2, 0, slice(212, 312), slice(8, 108)),
        (2, 1, slice(212, 312), slice(110, 210)),
        (2, 2, slice(212, 312), slice(212, 312)),
        (2, 3, slice(212, 312), slice(317, 417)),
        (2, 4, slice(212, 312), slice(419, 519)),
        (2, 5, slice(212, 312), slice(521, 621)),
        (2, 6, slice(212, 312), slice(626, 726)),
        (2, 7, slice(212, 312), slice(728, 828)),
        (2, 8, slice(212, 312), slice(830, 930)),
        (3, 0, slice(317, 417), slice(8, 108)),
        (3, 1, slice(317, 417), slice(110, 210)),
        (3, 2, slice(317, 417), slice(212, 312)),
        (3, 3, slice(317, 417), slice(317, 417)),
        (3, 4, slice(317, 417), slice(419, 519)),
        (3, 5, slice(317, 417), slice(521, 621)),
        (3, 6, slice(317, 417), slice(626, 726)),
        (3, 7, slice(317, 417), slice(728, 828)),
        (3, 8, slice(317, 417), slice(830, 930)),
        (4, 0, slice(419, 519), slice(8, 108)),
        (4, 1, slice(419, 519), slice(110, 210)),
        (4, 2, slice(419, 519), slice(212, 312)),
        (4, 3, slice(419, 519), slice(317, 417)),
        (4, 4, slice(419, 519), slice(419, 519)),
        (4, 5, slice(419, 519), slice(521, 621)),
        (4, 6, slice(419, 519), slice(626, 726)),
        (4, 7, slice(419, 519), slice(728, 828)),
        (4, 8, slice(419, 519), slice(830, 930)),
        (5, 0, slice(521, 621), slice(8, 108)),
        (5, 1, slice(521, 621), slice(110, 210)),
        (5, 2, slice(521, 621), slice(212, 312)),
        (5, 3, slice(521, 621), slice(317, 417)),
        (5, 4, slice(521, 621), slice(419, 519)),
        (5, 5, slice(521, 621), slice(521, 621)),
        (5, 6, slice(521, 621), slice(626, 726)),
        (5, 7, slice(521, 621), slice(728, 828)),
        (5, 8, slice(521, 621), slice(830, 930)),
        (6, 0, slice(626, 726), slice(8, 108)),
        (6, 1, slice(626, 726), slice(110, 210)),
        (6, 2, slice(626, 726), slice(212, 312)),
        (6, 3, slice(626, 726), slice(317, 417)),
        (6, 4, slice(626, 726), slice(419, 519)),
        (6, 5, slice(626, 726), slice(521, 621)),
        (6, 6, slice(626, 726), slice(626, 726)),
        (6, 7, slice(626, 726), slice(728, 828)),
        (6, 8, slice(626, 726), slice(830, 930)),
        (7, 0, slice(728, 828), slice(8, 108)),
        (7, 1, slice(728, 828), slice(110, 210)),
        (7, 2, slice(728, 828), slice(212, 312)),
        (7, 3, slice(728, 828), slice(317, 417)),
        (7, 4, slice(728, 828), slice(419, 519)),
        (7, 5, slice(728, 828), slice(521, 621)),
        (7, 6, slice(728, 828), slice(626, 726)),
        (7, 7, slice(728, 828), slice(728, 828)),
        (7, 8, slice(728, 828), slice(830, 930)),
        (8, 0, slice(830, 930), slice(8, 108)),
        (8, 1, slice(830, 930), slice(110, 210)),
        (8, 2, slice(830, 930), slice(212, 312)),
        (8, 3, slice(830, 930), slice(317, 417)),
        (8, 4, slice(830, 930), slice(419, 519)),
        (8, 5, slice(830, 930), slice(521, 621)),
        (8, 6, slice(830, 930), slice(626, 726)),
        (8, 7, slice(830, 930), slice(728, 828)),
        (8, 8, slice(830, 930), slice(830, 930)),
    ],
)
def test_calculate_calculate_image_place_works_properly(row, col, expected_row, expected_col):
    # WHEN
    image_place = calculate_image_place(row, col)

    # THEN
    assert image_place[0] == expected_row
    assert image_place[1] == expected_col
