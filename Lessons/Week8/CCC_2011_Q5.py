# CCC 2011 J5 Unfriend
# Kavan Lam
# For this question this website is very useful https://www.mathsisfun.com/sets/power-set.html

# Get the input and build a data structure to map who invited who
invite_map = {}
N = int(input())
for i in range(N):
    invite_map[i + 1] = []

for i in range(N - 1):
    person_num = int(input())
    invite_map[person_num].append(i + 1)

# Define a helper function to help determine if a given subset is possible
def subset_is_possible(subset):
    global invite_map
    for person_num in subset:
        invites = invite_map[person_num]  # Ensure each num in invites is in subset
        for num in invites:
            if not(num in subset):
                return False

    # If we get here then the subset is valid
    return True
    

# Generate all possible subsets of size 0 to N - 1 and check if it is possible
# We need to keep track of all the ones that are possible
num_of_possible_subsets = 0
num_of_good_subsets = 2 ** (N - 1)
people = [i + 1 for i in range(N - 1)]
for subset_num in range(num_of_good_subsets):
    # Build the binary mask for the people list
    binary = bin(subset_num)[2:]
    binary = ("0" * (N - 1 - len(binary))) + binary
    binary_mask = list(binary)

    # Apply the binary mask to generate the subset
    subset = [person_num for person_num, bit in zip(people, binary_mask) if bit == "1"]

    # Now determine of the subset is possible
    if (subset_is_possible(subset) == True):
        num_of_possible_subsets += 1
        
# Print the answer
print(num_of_possible_subsets)
