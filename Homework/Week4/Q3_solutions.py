# Question 3 Solutions
# 2D Grid Of Ones question
# Kavan Lam
# Oct 16, 2021

# We will use BFS to find the smallest number of moves needed.
# Remeber that BFS is an iterative algorithm so we do not need recursion.
# Our nodes will be represented by an ordered pair (i, j) where i and j
# represent the row index and column index respectively.
# This means our starting node should always be (0, 0)

# We will use deque to improve performace (this is not required)
from collections import deque

# Some sample test grids that we can use
grid1 = [[1, 0], [0, 1]]
grid2 = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
grid3 = [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [1, 1, 0, 1]]
grid4 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 0, 1]]

def get_neighbours(grid, current_node):
    neighbours = []
    
    row = current_node[0]
    col = current_node[1]
    num_of_moves = current_node[2] + 1

    max_row = len(grid) - 1
    max_col = max_row
    

    # Case 1: Move up
    if row - 1 >= 0 and grid[row - 1][col] == 1:
        new_node = (row - 1, col, num_of_moves)
        neighbours.append(new_node)

    # Case 2: Move down
    if row + 1 <= max_row and grid[row + 1][col] == 1:
        new_node = (row + 1, col, num_of_moves)
        neighbours.append(new_node)

    # Case 3: Move left
    if col - 1 >= 0 and grid[row][col - 1] == 1:
        new_node = (row, col - 1, num_of_moves)
        neighbours.append(new_node)

    # Case 4: Move right
    if col + 1 <= max_col and grid[row][col + 1] == 1:
        new_node = (row, col + 1, num_of_moves)
        neighbours.append(new_node)
    
    return neighbours

def find_smallest_number_of_moves(grid, start_node, target_node):
    num_of_moves = 0

    visited = set()
    visited.add(start_node)
    
    queue = deque()
    queue.append((start_node[0], start_node[1], num_of_moves))

    while len(queue) > 0:
        # Get the current node which also has the number of moves used to get there as the 3rd element
        current_node = queue.popleft()

        # Check if the current node matches the target
        if current_node[0:2] == target_node:
            return current_node[2] 

        # Continue searching by travelling to the neighbouring nodes
        neighbours = get_neighbours(grid, current_node)
        for node in neighbours:
            # We should also use this node if we have not already visited it
            if node[0:2] not in visited:
                visited.add(node[0:2])
                queue.append(node)

    return "Not Possible"


start_node = (0, 0)
target_node = (len(grid1) - 1, len(grid1) - 1)
print(find_smallest_number_of_moves(grid1, start_node, target_node))

start_node = (0, 0)
target_node = (len(grid2) - 1, len(grid2) - 1)
print(find_smallest_number_of_moves(grid2, start_node, target_node))

start_node = (0, 0)
target_node = (len(grid3) - 1, len(grid3) - 1)
print(find_smallest_number_of_moves(grid3, start_node, target_node))

start_node = (0, 0)
target_node = (len(grid4) - 1, len(grid4) - 1)
print(find_smallest_number_of_moves(grid4, start_node, target_node))



