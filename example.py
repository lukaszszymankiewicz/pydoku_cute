from src.drawing import draw_sudoku
from src.generators.utils import Difficult
from src.generators import generate


sudoku, solved_sudoku = generate(Difficult.hard)

draw_sudoku(sudoku, path="./sudoku.png")
draw_sudoku(solved_sudoku, path="./sudoku_solved.png")
