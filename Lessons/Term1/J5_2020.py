# Python CCC
# J5 2020 Escape Room
# Kavan Lam
# Feb 12, 2022
# Version 1 (bad solution)

from collections import deque

# First get the inputs
M = int(input())
N = int(input())
grid = []
for rowNum in range(M):
    grid.append(input().split(" "))

# Create a mapping from cell number to the cells we can jump to
def getListOfGoodCells(cellNum, M, N):
    goodCells = []
    for r in range(1, cellNum + 1):
        if cellNum % r == 0:
            c = cellNum // r
            if r <= M and c <= N:
                goodCells.append((r, c))
    return goodCells

numToCellMap = {}
for row in grid:
    for cellNum in row:
        if cellNum not in numToCellMap:
            numToCellMap[cellNum] = getListOfGoodCells(int(cellNum), M, N)

# Use BFS to traverse through the escape room
# We know we can not escape if we reach a point where there are no
# more nodes to serve from the queue and we have yet to reach (M, N)
queue = deque()
queue.append((1, 1))
visited = set()
visited.add((1, 1))
reachedEnd = False

while len(queue) > 0:
    current = queue.popleft()
    
    cells = numToCellMap[grid[current[0] - 1][current[1] - 1]]
    for cell in cells:
        if cell == (M, N):
           reachedEnd = True
           break
        if cell not in visited:
            visited.add(cell)
            queue.append(cell)


if reachedEnd:
    print("yes")
else:
    print("no")


    
