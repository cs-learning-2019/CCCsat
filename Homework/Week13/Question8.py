# Python CCC
# Question 8
# Kavan Lam
# Dec 29, 2021

# Below is a sample implmentation of the disjoint set data structure
# using a Python dictionary (hash map/table).
# We will use this data structure to solve this problem
class DisjointSet:
    # Define the attributes
    parent = {}
    rank = {}
    number_of_groups = 0

    # Adds items to the disjoint set by making each item its own set
    def makeSet(self, items):
        for item in items:
            # The representative each set will be the item itself
            self.parent[item] = item

            # The rank of each set starts at 0
            self.rank[item] = 0

            # We start of with max number of groups
            self.number_of_groups += 1

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

        self.number_of_groups -= 1
        

    # Prints the current state of the disjoint set 
    def printSets(self):
        for key in self.parent:
            print("The item: " + str(key) + " is represented by " + str(self.find(key)))


def count_num_groups(student_names, student_pairs):
    ds = DisjointSet()
    ds.makeSet(student_names)
    for pair in student_pairs:
        ds.union(pair[0], pair[1])

    return ds.number_of_groups


student_names = ["Abby", "Bob", "Kevin", "Lin", "Kate", "Lily"]
student_pairs = [("Abby", "Bob"), ("Lin", "Bob"), ("Lin", "Abby"), ("Kate", "Lily")]
print("The number of groups is " + str(count_num_groups(student_names, student_pairs)))








