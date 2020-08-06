Sudoku Generator (and solver)

1. How it works.
    Sudoku puzzle is 9x9 cells frame. Every cell can be filled with one number from 1 to 9. The
    objective of the game is to fill empty cells with appriopriate numbers. 

    Code holds every number put into every cell and possible legal numbers to be put into. 

    Of course, when some cell is filled, its state is "fixed", and and there is no possible numbers
    for this cell. 

    For every empty cell possibles are generated, and trimmed by other numbers in sudoku. For
    example if there is number "1" in some row in sudoku, every other "1" should be trimmed from
    possibles in this row (cause there will be only one number is nevery row). 
    Such operation is repeated for rows, cells and 3x3 squares (as sudoku rules stated).

    Program holds filled cells in Sudoku object (9x9 array) and possible numbers in PossibleMatrix
    objects (9x9x9 array). Most basic way to solve it is to look for "lonely" numbers in every cell,
    row and square. For example, looking for some row in Possible matrix we found that number "3"
    occurs only one in this row, that means that this value needs to be put there (cause every
    number must be unique). Such operation is done for every rows and columns and every cell (if
    there is only single possibility in cell, this number must be there), while possible matrix is
    updated after every new number in array. 
    Such solver works only for such Sudokus which have only one answer. 

    For harder sudoku (which can have more than one answer) recursive approach is taken. If solver
    find out that naive solving failes it founds out most promising cell (with least number of
    possibles) and generates alteration using every possibles.

    Generating sudoku is most tricky part. First, some numbers are put randomly over board, after
    that it is solved using recursive approach. After that number by number is emptied from this
    solved sudokui after it can be solved using naive approach. As a result sudoku with single
    solution is achieved (both wit hsolution). To generate harder puzzles, as a last step some
    numbers are taken from single-solution puzzle.

2. How it is drawn?
    All images are archived as compressed numpy array. Manipulation of these object (placing numbers
    imaages on board) is also achieved using numpy (we treat image as 2 dimensional array). As a
    final step array (filled with numbers) is converted into png image using pypng library.

3. How to use it?\
    a) clone (or download) repo'
    b) create virtual environment and install requirements from requirements.txt
        pip install -r requirements.txt
    c) run script in terminal by using command:\
        python pydoku.py\
    sudoku puzzle with solution will be gneerated in current format\\

    To generate harder sudoku (default difficult is easy), jus t parse appriopriate argument:\
        python sydoku --difficult=hard\\

    There are four difficulties: easy, medium, hard and immpossible\\

4. Have fun!
