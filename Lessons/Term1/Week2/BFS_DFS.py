# We can use the deque class for a stack and queue
# stack will use the pop method
# queue will use the popleft method
# This has better perfomance when compared to using a list directly
from collections import deque

# We will use an adjacency list to represent the graph
# For more on adj list refer to https://www.programiz.com/dsa/graph-adjacency-list
my_graph = {0:[9, 7, 11], 9:[0, 10, 8], 10:[9, 1], 8:[9, 1, 12], 1:[10, 8],
     12:[8, 2], 2:[12, 3], 3:[2, 7], 7:[3, 0, 11], 11:[0, 7]}

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
   

# DFS Recursive Method -----------------------------------------------------------
visited = set()

def dfs(G, node):
    if node in visited:
        return

    visited.add(node)
    print(node, end=" ")

    if node not in G:
        return
    
    neighbours = G[node]
    for next_node in neighbours:
        dfs(G, next_node)


# DFS Iterative Method -----------------------------------------------------------
def dfs_iterative(G, start_node):
    stack = deque()
    stack.append(start_node)

    visited = set()
    visited.add(start_node)

    while len(stack) > 0:
        current = stack.pop()
        print(current, end=" ")

        # This is not actually required, but just in case since there might be a mistake in my_graph
        if current not in G:
            pass
        
        neighbours = G[current]
        for node in neighbours:
            if node not in visited:
                visited.add(node)
                stack.append(node)
        

# Run the code -------------------------------------------------------------------
print("BFS")
bfs(my_graph, 0)
print("")

print("DFS Recursive")
dfs(my_graph, 0)
print("")

print("DFS Iterative")
dfs_iterative(my_graph, 0)



