from app.file_helpers import generate_sudokus_filenames


def test_generate_sudokus_filenames_works_properly():
    # WHEN
    filename1, filename2 = generate_sudokus_filenames()

    # THEN
    assert isinstance(filename1, str)
    assert isinstance(filename2, str)
