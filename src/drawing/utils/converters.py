import png


def convert_array_to_png_image(array, file_path: str):
    png.from_array(array, mode="L").save(file_path)
