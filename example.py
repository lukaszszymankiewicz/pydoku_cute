import time

from src.drawing import draw_sudoku
from src.generators.generator import generate


sudoku = generate()
result = draw_sudoku(sudoku, path="./result_yxx.png")
