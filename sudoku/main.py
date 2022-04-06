import numpy
import sudoku_functions
## Rules of sudoku
# Cannot have smae number in row
# Cannot have same number in column
# Cannot have same number in 3x3 square

## Recurrsion
# The function to solve the puzzle will use recurrsion
# The function will be called from within itself
board = [
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,3],
    [0,7,4,0,8,0,0,0,0],
    [0,0,0,0,0,3,0,0,2],
    [0,8,0,0,4,0,0,1,0],
    [6,0,0,5,0,0,0,0,0],
    [0,0,0,0,1,0,7,8,0],
    [5,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,4,0]
]
print("BEFORE")
sudoku_functions.print_board(board)
print("AFTER")
print("-------------------------------")
sudoku_functions.solve(board)
