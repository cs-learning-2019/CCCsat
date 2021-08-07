# Tic tac toe question
# Kavan Lam
# Aug 7, 2021

# NOTE 1: This question assumes o will move next
# NOTE 2: Do not consider this as a tic tac toe checker as it is incomplete.
#         This is meant to be an exercise working with 2D lists

# From this grid it should be o's turn next
grid = [["o", "", ""], ["x", "o", "x"], ["x", "", ""]]

# Define helper function
def check_if_winning_move(row, col, grid):
    grid[row][col] = "o"
    
    # Check up-down direction
    number_of_o = [grid[0][col], grid[1][col], grid[2][col]].count("o")
    if (number_of_o == 3):
        return True

    # Check left-right direction
    number_of_o = grid[row].count("o")
    if (number_of_o == 3):
        return True

    # Check positive-diagonal direction
    number_of_o = [grid[0][2], grid[1][1], grid[2][0]].count("o")
    if (number_of_o == 3):
        return True

    # Check negative-diagonal direction
    number_of_o = [grid[0][0], grid[1][1], grid[2][2]].count("o")
    if (number_of_o == 3):
        return True

    grid[row][col] = ""

    return False

# Check to see if o has a winning move and which spot
has_winning_move = False
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "":
            # Check to see if that spot (row, col) is a winning move for o
            if check_if_winning_move(row, col, grid) == True:
                print("Yes we have a winning move!")
                print("Row = " + str(row) + " Col = " + str(col))
                has_winning_move = True

if has_winning_move == False:
    print("No winning move :(")







    
