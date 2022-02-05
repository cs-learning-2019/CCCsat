# CCC J5 2019 Rule of Three
# Kavan Lam
# Oct 2, 2021

# First setup the data structures that we need
rule_src = []
rule_dst = []

# We need a data structure to store the nodes that we already visited
# We need 16 sets since S <= 15 and the first set will be for the starting node
visited = [set() for i in range(16)]

# Get and process the three rules
for i in range(3):
    rule = input().split()
    rule_src.append(rule[0])
    rule_dst.append(rule[1])

# Get and process the 4th line of input which is of the form S I F
SIF = input().split()
S = int(SIF[0])
I = SIF[1]
F = SIF[2]

# Define a helper function which produces all the node/states we can get to
# from cur_word by subbing all occurrences of src with dst.
# We return a list of all the new nodes/state
def find_new_nodes(cur_word, src, dst, rule_num):
    new_nodes = []

    if len(cur_word) >= len(src):
        for index in range(len(cur_word) - len(src) + 1):
            if cur_word[index:index + len(src)] == src:
                new_word = cur_word[:index] + dst + cur_word[index + len(src):]
                new_nodes.append([rule_num + 1, index + 1, new_word])
            
    return new_nodes

# Use recursive DFS to solve this problem
# Use the recursion_stack to backtrack and find the moves leading up to the target
def DFS_find_moves(cur_word,  cur_step_num, recursion_stack):
    # Base case for recursive function
    if cur_step_num > S or cur_word in visited[cur_step_num]:
        return False

    # Add the cur_word to the visisted list
    visited[cur_step_num].add(cur_word)

    # Check if we reached our target string if the current number of steps is correct
    if cur_step_num == S:
        if cur_word == F:
            for node in recursion_stack:
                print(node[0], node[1], node[2])
            return True
        return False
    
    # Recursive step
    for rule_num in range(3):
        new_nodes = find_new_nodes(cur_word, rule_src[rule_num], rule_dst[rule_num], rule_num)
        for node in new_nodes:
            new_recursion_stack = recursion_stack.copy()  # Note that a shallow copy is fine
            new_recursion_stack.append(node)
            if DFS_find_moves(node[2],  cur_step_num + 1, new_recursion_stack) == True:
                return True

# Start DFS on the provided starting node
DFS_find_moves(I, 0, [])
