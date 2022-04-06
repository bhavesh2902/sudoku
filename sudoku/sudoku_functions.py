import gui

# Finds the index of empty squares in board
def find_empty(grid):
    # Len of grid in 0 to 8 = 9
    for i in range(len(grid)):
        # This is the columns of the grid
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return(i,j) # row, column
    # If no empty return false
    return False

# This function checks if a number is valid
# grid - The  board
# num - The number to try
# pos - A tuple for the 0 postions (row,col)
def valid(grid, num, pos):
    # check the row
    for i in range(len(grid[0])):
        # Check if the num is equal to any other in row
        # Check that its not the one you just added also
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # check the col
    for i in range(len(grid[0])):
        # Check if the num is equal to any other in row
        # Check that its not the one you just added also
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the 3x3 column
    # Divide the box up into x and y cords
    # The box's have cords then of:
    # (0,0),(0,1),(0,2)
    # (1,0),(1,1),(1,2)
    # (2,0),(2,1),(2,2)
    # // is integer divide
    # Get which x co-ord by dividing col num by 3
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Loop through the box and make sure same element is not there
    # First get to the y index, need to multiply by 3 as box_y is
    # 0,1 or 2 but working with a 9x9 matrix
    # Add 3 then as last element will not be included
    for i in range(box_y*3, box_y*3 + 3):
        # Need to do same with X cord
        for j in range(box_x * 3, box_x*3 +3):
            # Check if the num is equal to any other in row
            # Check that its not the one you just added also
            if grid[i][j] == num and (i,j) != pos:
                return False
    return True

## print_board ##

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")



# This function solves the board
# grid - The playing board to be solved
# entrys - List of the boxes to fill in the gui mode
def solve(grid,entrys):
    # Find an empty place
    find = find_empty(grid)
    # If find is empty, we have the solution, no more empty space
    if not find:
        print_board(grid)
        return True
    # Keep Recurrsion going
    else:
        row, col = find
        # Now loop through values 1-9 to
        # attempt to put them in the solution
        for i in range(1,10):
            # Check if this value if valid at this position
            if valid(grid,i,(row,col)):
                # It's valid therfore put in the board
                grid[row][col] = i # THIS IS WHERE SOLUTION IS PLACED
                gui.update_square(row,col,i,entrys)

                # Will be true if no more blank spaces
                if solve(grid,entrys):
                    return True
                # If we have gotten to this point reset this value to 0
                # As the value at this index is not valid
                grid[row][col] = 0 #NEED TO DELETE VALUE AS IT IS NOT VALID
        return False

