class Result:
    def __init__(
        self,
        sudoku=None,
        solved: bool = False,
        nodes: int = 1,
        branches: int = 1,
        time_needed: float = 0.0,
    ):
        self._sudoku = sudoku
        self._solved = solved
        self.nodes = nodes
        self.branches = branches
        self.time_needed = time_needed

    @property
    def sudoku(self):
        return self._sudoku

    @property
    def is_solved(self):
        return self._solved
