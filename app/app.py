import os

from flask import Flask, jsonify, render_template, request

from .file_helpers import delete_unused_sudokus
from .file_paths import SOLVED_SUDOKU_PATH, UNSOLVED_SUDOKU_PATH
from .form_helpers import get_difficult_from_request
from .src import Difficult, draw_sudoku, generate

delete_unused_sudokus()
app = Flask(__name__)
app.config.from_object(os.environ.get("APP_CONFIG"))


@app.route("/generate_new_puzzle")
def generate_new_puzzle():
    delete_unused_sudokus()

    difficult = get_difficult_from_request(request.args)
    solved_sudoku, unsolved_sudoku = generate(difficult)

    draw_sudoku(solved_sudoku, path=SOLVED_SUDOKU_PATH)
    draw_sudoku(unsolved_sudoku, path=UNSOLVED_SUDOKU_PATH)

    return jsonify("nothing")


@app.route("/")
def main():
    return render_template(
        template_name_or_list="index.html",
        title="Pydoku - Sudoku generator",
        difficult=Difficult.default,
    )


if __name__ == "__main__":
    app.run()
