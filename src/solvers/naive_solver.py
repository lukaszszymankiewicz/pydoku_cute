from src.objects import Sudoku


def naive_solver(sudoku: Sudoku) -> Sudoku:

    while not sudoku.is_solved:
        candidates_rows, candidates_cols, candidates_nbrs = sudoku.find_sole_candidates()

        if candidates_rows.size == 0 and candidates_cols.size == 0 and candidates_nbrs.size == 0:
            return sudoku

        sudoku[candidates_rows, candidates_cols] = candidates_nbrs + 1

    return sudoku
