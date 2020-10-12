Sudoku Generator 

1. What is this?
    It is simple algorithm for generating Sudoku puzzles wrapped in simple flask app.
    Goal of this code is to provide well-written code for such use (most of the programs/scripts 
    for such use is rather rudimentally).

2. What is Sudoku?
    Sudoku puzzle is 9x9 cells frame. Every cell can be fill with one number from 1 to 9. The
    goal of the game is to fill empty cells with appropriate numbers. 

3. How it works?
    Code holds every number put into every cell and possible legal numbers to put into. 

    Of course, when some cell is fill, its state is "fixed", and and there is no possible numbers
    for this cell. 

    For every empty cell possibles are generate, and trimmed by other numbers in Sudoku. For
    example if there is number "1" in some row in Sudoku, every other "1" should be trim from
    possibles in this row (cause there will be only one number is every row). 
    Such operation is repeat for rows, cells and 3x3 squares (as Sudoku rules stated).

    Program hold filled cells in Sudoku object (9x9 array) and possible numbers in PossibleMatrix
    objects (9x9x9 array). Most basic way to solve it is to look for "lonely" numbers in every cell,
    row and square. For example, looking for some row in Possible matrix we found that number "3"
    occurs only one in this row, that means that this value needs to put there (cause every
    number must be unique). Such operation is made for every rows and columns and every cell (if
    there is only single possibility in cell, this number must be there), while possible matrix is
    updated after every new number in array. 
    Such solver works only for such Sudokus which have only one answer. 

    For harder Sudoku (which can have more than one answer) recursive approach is taken. If solver
    find out that naive solving failed it founds out most promising cell (with least number of
    possibles) and generates alteration using every possibles.

    Generating Sudoku is most tricky part. First, some numbers are put over board, after
    that it is solve using recursive approach. After that number by number is empty from this
    solved Sudoku after it can be solve using naive approach. As a result Sudoku with single
    solution is achieve (both with solution achieved earlier). To generate harder puzzles, as a last 
    step some numbers, are took from single-solution puzzle. This results in a puzzle which
    does not necessary have only one solution (and that is the goal!).
    
4. How it is draw?
    All images are archive as compressed numpy array. Manipulation of these object (placing numbers
    images on board) is also achieved using numpy (we treat image as 2 dimensional array). As a
    final step array (filled with numbers) is convert into png image using pypng library.

5. Copyrights
    Please, feel free to use app as you wish. Have fun!
