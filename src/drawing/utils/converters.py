import png

from src.static.types import Matrix, FilePath


def convert_array_to_png_image(matrix: Matrix, file_path: FilePath) -> None:
    png.from_array(matrix, mode="L").save(file_path)
