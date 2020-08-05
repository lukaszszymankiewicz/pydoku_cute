from numpy import load

EMPTY_FRAME_PATH = "src/static/images/empty_frame.npz"


def load_empty_frame():
    return load(EMPTY_FRAME_PATH)["empty_frame"]
