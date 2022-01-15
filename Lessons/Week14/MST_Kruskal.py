# Python CCC
# Kruskal's Algorithm for finding MST
# Kavan Lam
# Dec 18, 2021

# Below is an implementation of Kruskal's Algorithm using disjoint sets
# to find the MST of a undirected, connected and weighted graph given the
# set of vertices and set of edges in the form (x, y, w) where x and y are
# nodes and w is the weight. We let V be the set of vertices and E be the set of edges

# Also note that you could implement this in a brute force manner where we use DFS to detect if a cycle exist
# The brute force would be O(n^2)
# Using Disjoint sets we can get O(nLogn)

from DisjointSet import *

def findMST(V, E):
    # Define a data structure to store the MST (we simply use a list of edges)
    mst = []

    # Create and setup disjoint sets
    ds = DisjointSet()
    ds.makeSet(V)

    # Get a sorted list of all edges sorted by weight (smallest to largest)
    sortedEdges = sorted(E, key = lambda edge: edge[2])

    # Loop over the sorted edges and construct the MST
    for edge in sortedEdges:
        x = edge[0]
        y = edge[1]

        # If the two vertices are not connected then connect them otherwise skip this edge
        # We know the two vertices are not connected if they are in different sets (they have different representatives)
        if ds.find(x) != ds.find(y):
            mst.append(edge)
            ds.union(x, y)

    return mst

# Define test graph
V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
E = [(1, 2, 4),
     (1, 8, 8),
     (2, 8, 11),
     (2, 3, 8),
     (3, 9, 2),
     (8, 9, 7),
     (7, 8, 1),
     (7, 9, 6),
     (3, 4, 7),
     (3, 6, 4),
     (6, 7, 2),
     (4, 6, 14),
     (4, 5, 9),
     (5, 6, 10)
     ]

mst = findMST(V, E)
for edge in mst:
    print(edge)


    
