import argparse

from datetime import datetime

from src.drawing import draw_sudoku
from src.generators.utils import Difficult
from src.generators import generate

parser = argparse.ArgumentParser(description="generates sudoku puzzle")
parser.add_argument(
    "--difficulty",
    default=Difficult.easy,
    type=str,
    help="sudoku difficulty: easy(default), medium, hard, immposible",
)
args = parser.parse_args()

if args.difficulty not in Difficult.legal_difficulties:
    raise AttributeError("Difficult not recognized!")

sudoku, solved_sudoku = generate(args.difficulty)
time_stamp = datetime.now().strftime("%d%m%Y%H%M%S")
draw_sudoku(sudoku, path=f"./{time_stamp}_sudoku.png")
draw_sudoku(solved_sudoku, path=f"./{time_stamp}_sudoku_solved.png")
