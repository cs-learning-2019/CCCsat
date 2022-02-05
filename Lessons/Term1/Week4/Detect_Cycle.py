# Cycle detection using DFS
# We can use DFS to detect if a graph contains any cycles.

# Note: WE WILL ASSUME THAT OUR GRAPHS ARE CONNECTED if it is non-directed
# For directed graphs you do not need to code the part where we loop over all the nodes
# to ensure all nodes are visited.

# We can use either use the recursive or iterative approche to DFS
# We will only do the recursive method
# Note: that it matters whether the graph is directed or not
# Note: a cycle will have at 3 nodes in undirected graph
# For a directed graph it is a bit more complicated
# We can have self-loops and 2 node loop
# The question is do we consider these cycles?
# For our class we will say YES

non_directed_no_cycle_graph = {1:[2, 3], 2:[1, 4], 3:[1], 4:[2]}
non_directed_cycle_graph = {1:[2, 3], 2:[1, 4], 3:[1, 4], 4:[2, 3]}

def recursive_find_cycle_non_directed(G, node, parent):
    if node in visited:
        return False

    visited.add(node)
    
    neighbours = G[node]
    for next_node in neighbours:
        if next_node in visited and next_node != parent:
            return True
        
        if recursive_find_cycle_non_directed(G, next_node, node) == True:
            return True

    return False

visited = set()
print(recursive_find_cycle_non_directed(non_directed_no_cycle_graph, 1, -99))
visited = set()
print(recursive_find_cycle_non_directed(non_directed_cycle_graph, 1, -99))


# Here is some test data for directed
directed_no_cycle_graph = {1:[2, 3], 2:[4], 3:[4], 4:[]}
directed_cycle_graph = {1:[2, 3], 2:[4], 3:[4], 4:[5], 5:[3]}
# So what is the idea behind detecting a cycle in a directed graph
# Hint: recursion stack



