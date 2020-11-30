import os

from flask import Flask, render_template, request

from .file_helpers import delete_unused_sudokus, generate_sudokus_filenames
from .file_paths import EMPTY_FRAME_FILE_PATH
from .form_helpers import get_difficult_from_request
from .src import draw_sudoku, generate
from .src.enums import Difficult

app = Flask(__name__)
app.config.from_object(os.environ.get("APP_CONFIG"))


@app.route("/generate_new_puzzle")
def generate_new_puzzle():
    delete_unused_sudokus()

    difficult = get_difficult_from_request(request.args)

    solved_sudoku, unsolved_sudoku = generate(difficult=difficult)
    solved_sudoku_file_path, unsolved_sudoku_file_path = generate_sudokus_filenames()

    draw_sudoku(solved_sudoku, path=solved_sudoku_file_path)
    draw_sudoku(unsolved_sudoku, path=unsolved_sudoku_file_path)

    return "nothing"


@app.route("/")
def main():
    delete_unused_sudokus()

    return render_template(
        template_name_or_list="index.html",
        title="Pydoku - Sudoku generator",
        difficult=Difficult.default,
    )


if __name__ == "__main__":
    app.run()
