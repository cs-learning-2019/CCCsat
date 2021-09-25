# CCC 2021 J5 Modern Art
# Kavan Lam
# Sept 19, 2021

# First get the inputs
M = int(input())
N = int(input())
K = int(input())

# Initialize the dictonaries that will store information about the moves
rows = {}
cols = {}
for row_num in range(M):
    rows[row_num + 1] = 0
    
for col_num in range(N):
    cols[col_num + 1] = 0

# Process the K lines of choices and store the moves in the dictonaries
for i in range(K):
    # Get the choice and break it into 2 parts
    choice = input()
    axis = (choice.split(" "))[0]
    num = (choice.split(" "))[1]

    # Update the corresponding dictionary
    if axis == "R":
        rows[int(num)] = rows[int(num)] + 1
    else:
        cols[int(num)] = cols[int(num)] + 1

# Now loop over each cell and count how many are gold
num_of_gold_cells = 0
for row in range(M):
    for col in range(N):
        num_of_flips_for_cell = rows[row + 1] + cols[col + 1]
        if num_of_flips_for_cell % 2 != 0:
            num_of_gold_cells += 1

# Print the answer
print(num_of_gold_cells)
        
    
    
