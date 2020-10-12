import os

basedir = os.path.abspath(os.path.dirname(__file__))


class LocalConfig(object):
    TESTING = True
    CSRF_ENABLED = True
    USER_APP_NAME = "Pydoku - Sudoku generator"


class ProductionConfig(object):
    TESTING = False
    CSRF_ENABLED = True
    USER_APP_NAME = "Pydoku - Sudoku generator"
