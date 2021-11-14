## Sudoku Generator 

### Pydoku
    To see app in full glory, visit: https://pydoku.herokuapp.com/

### What is this?
    It is algorithm for generating Sudoku puzzles (resulted as downloadable png images) wrapped in 
    simple web app.
    Goal of this project is to provide well-written code for such use (most of the programs/scripts 
    for solving/generating sudokus are rather rudimentally).

### What is Sudoku?
    Sudoku is a logic-based, combinatorial number-placement puzzle. In classic sudoku, the 
    objective is to fill a 9×9 grid with digits so that each column, each row, and each 
    of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions")
    contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid,
    which for a well-posed puzzle has a single solution. 

### Algorithm
    Code holds every number put into every cell and possible legal numbers to put into empty cells. 

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
    
### How it is drawn?
    All images are archived as compressed numpy array. Generating resulted Sudoku image is also 
    achieved using numpy (we treat image as 2 dimensional array). Converting these numpy array to 
    png image is achieved by pypng library.

### Copyrights
    Please, feel free to use app as you wish. Have fun!
