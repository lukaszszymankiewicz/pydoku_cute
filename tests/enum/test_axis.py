from pydoku.enum import Axis


def test_axis_enum_works_properly():
    # GIVEN
    expected_result_for_column = 1
    expected_result_for_row = 0
    expected_result_for_number = 2

    # WHEN
    result_for_column = Axis.column
    result_for_row = Axis.row
    result_for_number = Axis.number

    # THEN
    assert result_for_column == expected_result_for_column
    assert result_for_row == expected_result_for_row
    assert result_for_number == expected_result_for_number
