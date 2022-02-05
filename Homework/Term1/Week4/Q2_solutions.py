# Question 2 Solutions
# Detect a cycle in a directed graph using recursive dfs from a given starting node
# Kavan Lam
# Oct 16, 2021

# Note: we do NOT loop over all the nodes outside of DFS to ensure that all
# nodes have been visited. This is to simplify the problem.
# You can really think of the question then as asking whether or not
# we can enter a cycle from some given starting node in the graph.

def recursive_find_cycle_directed(G, node, recursive_stack):
    if node in visited:
        return False

    visited.add(node)
    recursive_stack.append(node)
    
    neighbours = G[node]
    for next_node in neighbours:
        if next_node in recursive_stack:
            return True

        new_recursive_stack = recursive_stack.copy()
        
        if recursive_find_cycle_directed(G, next_node, new_recursive_stack) == True:
            return True

    return False



directed_no_cycle_graph = {1:[2, 3], 2:[4], 3:[4], 4:[]}
directed_cycle_graph = {1:[2, 3], 2:[4], 3:[4], 4:[5], 5:[3]}

visited = set()
recursive_stack = []
print(recursive_find_cycle_directed(directed_no_cycle_graph, 1, recursive_stack))

visited = set()
recursive_stack = []
print(recursive_find_cycle_directed(directed_cycle_graph, 1, recursive_stack))

