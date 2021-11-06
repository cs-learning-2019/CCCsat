# Python CCC
# J5 2017 Nailed It
# Kavan Lam
# Oct 30, 2021

# First get the input
N = int(input())
wood = input().split(" ")

# Create data structures to hold on to data
size_to_number_of_wood = [0] * 2001
heights_to_number_of_boards = [0] * 4001

# Process the wood input (list of given wood sizes)
# We need to count how many pieces of wood we have of each size
for wood_size in wood:
    size_to_number_of_wood[int(wood_size)] += 1

# Determine the number of boards we can create for each size
for height in range(2, len(heights_to_number_of_boards)):
    total = 0
    if height % 2 == 0:
        for i in range(1, (height // 2) + 1):
            j = height - i
            if j > 2000:
                continue
            elif i == j:
                total += size_to_number_of_wood[i] // 2
            else:
                total += min(size_to_number_of_wood[i], size_to_number_of_wood[j])
    else:
        for i in range(1, ((height - 1) // 2) + 1):
            j = height - i
            if j > 2000:
                continue
            elif i == j:
                total += size_to_number_of_wood[i] // 2
            else:
                total += min(size_to_number_of_wood[i], size_to_number_of_wood[j])
        
    heights_to_number_of_boards[height] = total
    

# Get the longest length of fence and how many different height can be used
longest_length = 0
number_of_possible_heights = 0
for height in range(0, len(heights_to_number_of_boards)):
    if heights_to_number_of_boards[height] > longest_length:
        longest_length = heights_to_number_of_boards[height]
        number_of_possible_heights = 1
    elif heights_to_number_of_boards[height] == longest_length:
        number_of_possible_heights += 1

# Print the answer
print(longest_length, number_of_possible_heights)
