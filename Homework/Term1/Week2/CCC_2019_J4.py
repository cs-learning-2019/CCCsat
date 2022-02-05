# CCC 2019 J4 Flipper
# Kavan Lam
# Oct 1, 2021

# First get the input
moves = input()

# We can actually simplify the moves by using the fact that two H or two V
# will cancel due to symmetry. This won't matter too much for this question
# but if the computational complexity of processing a single flip was
# expensive then this optimization is very important.
new_moves = ""
for move in moves:
    if new_moves == "" or new_moves[-1] != move:
        new_moves += move
    elif new_moves[-1] == move:
        new_moves = new_moves[0:-1]
    
# Process the moves
grid = [["1", "2"], ["3", "4"]]
for move in new_moves:
    if move == "H":
        grid = [grid[1], grid[0]]
    else:
        grid = [grid[0][::-1], grid[1][::-1]]

# Print the final orientation
print(grid[0][0] + " " + grid[0][1])
print(grid[1][0] + " " + grid[1][1])


    
