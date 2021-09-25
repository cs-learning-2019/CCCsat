# CCC 2021 J4 Arranging Books
# Kavan Lam
# Sept 18, 2021

# First get the single line of input
books = input()

# Go through the list of unordered books and find out how much of each type we have
L = 0
M = 0
S = 0
for book in books:
    if book == "L":
        L += 1
    elif book == "M":
        M += 1
    else:
        S += 1

# Now determine the number of swaps required for each type of book size
L_swaps = 0
M_swaps = 0
S_swaps = 0

# Consider the partition containing all the large books
for i in range(L):
    if books[i] == "M":
        M_swaps += 1
    elif books[i] == "S":
        S_swaps += 1

# Consider the partition containing all the small books
for i in range(len(books) - S, len(books)):
    if books[i] == "M":
        M_swaps += 1
    elif books[i] == "L":
        L_swaps += 1

# Output the answer
print(max(L_swaps, S_swaps) + M_swaps)
