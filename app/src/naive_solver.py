from .sudoku import Sudoku


def naive_solver(sudoku: Sudoku) -> Sudoku:
    """ Simplest sudoku solver.

    Finds cell in which only one number can be placed (looking in four dimensions: rows, columns,
    3x3 squares and cells). Such number is called "sole candidate", if is found somewhere in 
    given sudoku alogrithm is filling such number.

    Then, array is looking for another sole candidates which was created after filling all numbers
    from last step.

    If such algorithm cannot solve sudoku (there is not any sole candidates - every cell has at
    least two number shich can be put) such puzzle is returned (with all numbers which can be filled
    using this algorith).

    Difficult marked as "easy" represents puzzle which have only sole candidated to be filled.

    Args:
        sudoku - sudoku object.

    Returns:
        sudoku - sudoku object (all filled if algorithm succeded, and not filled if algorith failed)
    """
    while not sudoku.is_solved:
        candidates_rows, candidates_cols, candidates_nbrs = sudoku.find_sole_candidates()

        if candidates_rows.size == 0 and candidates_cols.size == 0 and candidates_nbrs.size == 0:
            return sudoku

        sudoku[candidates_rows, candidates_cols] = candidates_nbrs + 1

    return sudoku
