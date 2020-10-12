from random import shuffle

from .naive_solver import naive_solver
from .sudoku import Sudoku


def recursive_solver(sudoku: Sudoku) -> Sudoku:
    """This function represents brute-force algorithm for solving sudoku puzzle.

    It is using naive_solver to get the best approximation of solved puzzle. If naive solver failes
    to return proper answer, then most promising cell is chosen (such with least legal numbers of 
    possible numbers to be filled). Then all this numbers are used to create combinations of 
    original puzzle (each with different number placed in most promising cell).

    Each of combinations are put into naive_solver. Whole process is continuing while first proper
    result occurs.

    Because this algorithm is brute-force and detmirnistic, inputting very hard sudoku (for example
    with only 2 cells filled) will always return same solution.

    Attrs:
        sudoku - sudoku object.

    Returns:
        sudoku object which is solved.
    """
    sudokus = [sudoku]

    while True:
        result = naive_solver(sudokus.pop())

        if not result.is_solved:
            if result.is_solvable:
                cell_row, cell_col = result.get_most_promising_cell()
                possible_number = result.get_possible_numbers(cell_row, cell_col)
                new_sudokus = result.get_sudoku_combinations(cell_row, cell_col, possible_number)
                sudokus.extend(new_sudokus)
        else:
            if not result.is_valid:
                shuffle(sudokus)
            else:
                return result
