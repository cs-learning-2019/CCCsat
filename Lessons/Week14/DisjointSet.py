# Python CCC
# Disjoint Sets
# Kavan Lam
# Dec 18, 2021

# Below is a sample implmentation of the disjoint set data structure
# using a Python dictionary (hash map/table). Note: you can also implement
# disjoint sets using linked-lists but we have not learned that yet

class DisjointSet:
    # Define the attributes
    parent = {}
    rank = {}

    # Adds items to the disjoint set by making each item its own set
    def makeSet(self, items):
        for item in items:
            # The representative each set will be the item itself
            self.parent[item] = item

            # The rank of each set starts at 0
            self.rank[item] = 0

    # Finds and returns the representative of a given item
    # This implementation uses path compression
    def find(self, item):
        # If the item is not the parent them we must find the representative recursively
        if self.parent[item] != item:
            representative = self.find(self.parent[item])

            # For path compression we set the representative to the items we go through
            self.parent[item] = representative

        return self.parent[item]

    # Combine two sets together given two items
    # This implementation uses union by rank optimization
    def union(self, item1, item2):
        # First find the representative of the two items
        rep1 = self.find(item1)
        rep2 = self.find(item2)

        # If the reps are the same then do not have to do anything
        # since they are already in the same group
        if rep1 == rep2:
            return

        # We should always make the smaller rank piece a child of the bigger piece
        if self.rank[rep1] > self.rank[rep2]:
            self.parent[rep2] = rep1
        elif self.rank[rep1] < self.rank[rep2]:
            self.parent[rep1] = rep2
        else:
            self.parent[rep1] = rep2
            self.rank[rep2] = self.rank[rep2] + 1
        

    # Prints the current state of the disjoint set 
    def printSets(self):
        for key in self.parent:
            print("The item: " + str(key) + " is represented by " + str(self.find(key)))


if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]
    
    ds = DisjointSet()
    ds.makeSet(items)
    ds.printSets()
    ds.union(4, 3)
    ds.union(2, 1)
    ds.union(1, 3)
    print("")
    ds.printSets()

        
