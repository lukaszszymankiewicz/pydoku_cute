import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from .file_helpers import delete_unused_sudokus, generate_sudokus_filenames
from .file_paths import EMPTY_FRAME_FILE_PATH
from .src import draw_sudoku, generate
from .src.enums import Difficult
from .validation import validate_difficult

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ.get("APP_CONFIG"))


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template(
            template_name_or_list="index.html",
            title="Pydoku - Sudoku generator",
            solved_sudoku_file_path=EMPTY_FRAME_FILE_PATH,
            unsolved_sudoku_file_path=EMPTY_FRAME_FILE_PATH,
            difficult=Difficult.default,
        )

    else:
        delete_unused_sudokus()
        difficult = validate_difficult(request.form)

        solved_sudoku, unsolved_sudoku = generate(difficult=difficult)
        solved_sudoku_file_path, unsolved_sudoku_file_path = generate_sudokus_filenames()

        draw_sudoku(solved_sudoku, path=solved_sudoku_file_path)
        draw_sudoku(unsolved_sudoku, path=unsolved_sudoku_file_path)

        return render_template(
            template_name_or_list="index.html",
            title="Pydoku - Sudoku generator",
            solved_sudoku_file_path=solved_sudoku_file_path,
            unsolved_sudoku_file_path=unsolved_sudoku_file_path,
            difficult=difficult,
        )


if __name__ == "__main__":
    app.run()
