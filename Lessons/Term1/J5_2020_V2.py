# Python CCC
# J5 2020 Escape Room
# Kavan Lam
# Feb 12, 2022
# Version 2
# Python is too slow. Look here for C++ solution https://www.youtube.com/watch?v=J5vjQCWBnCU

from collections import deque

# First get the inputs
M = int(input())
N = int(input())
grid = []
for rowNum in range(M):
    grid.append(input().split(" "))

# Create a mapping from cell num to the list of possible prev cells
cellNumToPrevCells = {}
for r in range(1, M + 1):
    for c in range(1, N + 1):
        cellNum = grid[r - 1][c - 1]
        if cellNum not in cellNumToPrevCells:
            cellNumToPrevCells[cellNum] = [(r, c)]
        else:
            cellNumToPrevCells[cellNum].append((r, c))
        

queue = deque()
queue.append((M, N))
visited = set()
visited.add((M, N))
reachedStart = False

while len(queue) > 0:
    current = queue.popleft()
    product = str(current[0] * current[1])

    if product not in cellNumToPrevCells:
        continue
    
    cells = cellNumToPrevCells[product]
    for cell in cells:
        if cell == (1, 1):
           reachedStart = True
           break
        if cell not in visited:
            visited.add(cell)
            queue.append(cell)


if reachedStart:
    print("yes")
else:
    print("no")


    
