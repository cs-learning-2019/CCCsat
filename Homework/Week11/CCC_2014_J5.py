# Python CCC
# J5 2014 Assigning Partners
# Kavan Lam
# Dec 11, 2021

# First get the inputs
N = int(input())
names1 = input().split(" ")
names2 = input().split(" ")

# Create a mapping from second list to first list
mapping = {}

# Go through the two list of names and check if it is good
def helper():
    for index in range(N):
        if names1[index] == names2[index]:
            return "bad"

        if names1[index] in mapping:
            mapped_name = mapping[names1[index]]
            if names2[index] != mapped_name:
                return "bad"
            
        mapping[names2[index]] = names1[index]

    return "good"

print(helper())


    


