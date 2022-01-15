# Python CCC
# Question 3
# Kavan Lam
# Dec 29, 2021

visited = set()
max_dist_in_dfs = 0
def DFS_max_dist(G, node, depth):
    global max_dist_in_dfs
    
    if node in visited:
        return
    else:
        if max_dist_in_dfs < depth:
            max_dist_in_dfs = depth

    visited.add(node)
    
    neighbours = G[node]
    for next_node in neighbours:
        dist = DFS_max_dist(G, next_node, depth + 1)


def find_max_distance(graph):
    # Tell Python to look globally for these variables
    global visited
    global max_dist_in_dfs
    
    # Basically we want to run DFS once for each vertex acting as the starting vertex
    starting_vertices = list(graph.keys())
    max_dist = 0
    for vertex in starting_vertices:
        DFS_max_dist(graph, vertex, 0)
        if max_dist_in_dfs > max_dist:
            max_dist = max_dist_in_dfs
        visited = set()
        max_dist_in_dfs = 0

    return max_dist


graph = {1:[2, 4], 2:[1, 3, 5], 3:[2, 6], 4:[1, 7, 5], 5:[2, 4, 5], 6:[3, 5, 8, 9], 7:[4], 8:[6, 9], 9:[6, 8]}
print("The max distance between any two vertices is " + str(find_max_distance(graph)))


# For reference here is the DFS code from week 4
# DFS Recursive Method
"""
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
"""

