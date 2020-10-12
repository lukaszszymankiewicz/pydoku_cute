from ..types import Matrix


def sudoku_is_valid(array: Matrix) -> bool:
    """
    Tries to find if sudoku array is valid by iterating its rows and checking
    if there is some duplicates in values (if so the array is invalid).

    Args:
        array - 2d numpy array (9x9) representing values in sudoku grid.

    Returns:
        boolean value reprsenting if given sudoku array is valid.
    """
    for row in array:
        if len(set(row)) != len(row):
            return False
    return True
