# Python CCC
# Question 2
# Kavan Lam
# Dec 29, 2021

# For this we will let each cell be a vertex and the edges be the 8
# possible moves that we can take to move to a neighbouring cell
# A vertex is represented by a ordered pair (x, y) where x is the row
# and y is the column number.

from collections import deque

# This is just simple BFS (nothing special)
def BFS(mat, visited, x, y):
    # First create a queue data structure to store the cells that we will process
    # We need a queue since for BFS we want to finish looking at the neighbouring cells
    # before going any deeper unlike DFS
    queue = deque()
    queue.append((x, y))

    visited[x][y] = True

    while len(queue) > 0:
        current = queue.popleft()
        
        # Check each of the 8 potential neighbour cells and add them to the list of neighbours if they are valid
        # It is valid if it is not water and also within range
        neighbours = []
        num_of_rows = len(mat)
        num_of_cols = len(mat[0])
        x = current[0]
        y = current[1]
        # Check up
        if x - 1 >= 0 and mat[x - 1][y] == 1:
            neighbours.append((x - 1, y))
        # Check down
        if x + 1 < num_of_rows and mat[x + 1][y] == 1:
            neighbours.append((x + 1, y))
        # Check right
        if y + 1 < num_of_cols and mat[x][y + 1] == 1:
            neighbours.append((x, y + 1))
        # Check left
        if y - 1 >= 0 and mat[x][y - 1] == 1:
            neighbours.append((x, y - 1))
        # Check top-left
        if x - 1 >= 0 and y - 1 >= 0 and mat[x - 1][y - 1] == 1:
            neighbours.append((x - 1, y - 1))
        # Check top-right
        if x - 1 >= 0 and y + 1 < num_of_cols and mat[x - 1][y + 1] == 1:
            neighbours.append((x - 1, y + 1))
        # Check bottom-right
        if x + 1 < num_of_rows and y + 1 < num_of_cols and mat[x + 1][y + 1] == 1:
            neighbours.append((x + 1, y + 1))
        # Check bottom-left
        if x + 1 < num_of_rows and y - 1 >= 0 and mat[x + 1][y - 1] == 1:
            neighbours.append((x + 1, y - 1))
        
        for cell in neighbours:
            if visited[cell[0]][cell[1]] == False:
                visited[cell[0]][cell[1]] = True
                queue.append(cell)



def count_islands(mat):
    # Figure out how many rows and columns we have
    num_of_rows = len(mat)
    num_of_cols = len(mat[0])

    # Create a data structure to store which cells have already been visted
    visited = []
    for x in range(num_of_rows):
        visited.append([False for y in range(num_of_cols)])

    # Loop over all the cells from top to bottom, left to right
    num_of_islands = 0
    for x in range(num_of_rows):
        for y in range(num_of_cols):
            # If we have a cell that has not been visited and is not water then search from there
            if visited[x][y] == False and mat[x][y] == 1:
                num_of_islands += 1
                BFS(mat, visited, x, y)

    return num_of_islands
                

mat = [[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
       [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
       [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]]
 
print('The total number of islands is', count_islands(mat))



# Just a reminder from Week 4 this is our BFS code
# BFS ----------------------------------------------------------------------------
def bfs(G, start_node):
    queue = deque()
    queue.append(start_node)

    visited = set()
    visited.add(start_node)

    while len(queue) > 0:
        current = queue.popleft()
        print(current, end=" ")

        # This is not actually required, but just in case since there might be a mistake in my_graph
        if current not in G:
            pass
        
        neighbours = G[current]
        for node in neighbours:
            if node not in visited:
                visited.add(node)
                queue.append(node)

