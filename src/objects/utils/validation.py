from src.static.types import Matrix


def sudoku_is_valid(array: Matrix) -> bool:
    """
    Tries to find if sudoku array is valid by iterating its rows and checking
    if there is some duplicates in values (if so the array is invalid).
    """
    for row in array:
        if len(set(row)) != len(row):
            return False
    return True
