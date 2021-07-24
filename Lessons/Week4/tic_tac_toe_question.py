# Tic tac toe question
# Kavan Lam
# July 24, 2021

# From this grid it should be o's turn next
grid = [["o", "", ""], ["x", "o", "x"], ["x", "", ""]]

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
  
def check_if_winning_move(row, col, grid):
    pass # Work in progress
