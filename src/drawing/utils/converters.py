import png

from src.static.types import Matrix, FilePath


def convert_array_to_png_image(matrix: Matrix, file_path: FilePath) -> None:
    """
    Converts inuputted 2d numpy array into .png file.

    Args:
        matrix: 2d numpy array (must be 2d, and np.uint8 dtype!),
        file_path: place where resulted png will be saved.
    
    Returns:
        None
    """
    png.from_array(matrix, mode="L").save(file_path)
