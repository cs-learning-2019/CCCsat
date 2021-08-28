# CCC 2012 Coin Game Q5
# Kavan Lam Aug 26, 2021

# Define a Node class to represent a state in the coin game
class Node:
    def __init__(self, initial_pos = []):
        self.state = [[num] for num in initial_pos]
        self.num_of_moves = 0
            

# Define a helper function to check if a node's state matches our target
def check_state(node, target_state):
    if node.state == target_state:
        return True
    else:
        return False

# Define a helper function to check if a given node state has already been visited
# Return False if a dup is found and True otherwise
def check_for_dup(new_node, queue):
    for node in queue:
        if node.state == new_node.state:
            return False

    # If we get here then there is no dup
    return True


# This is the main loop
while True:
    # Get the input (note: we stop the program when n is zero)
    n = int(input())
    if n == 0:
        break
    
    initial_pos = input().split(" ")
    initial_pos = [int(num) for num in initial_pos]
    
    # Define some variables in preperation for BFS
    starting_node = Node(initial_pos)
    queue = [starting_node]
    queue_pos = 0
    min_moves = -1
    
    initial_pos.sort()
    target_state = [[num] for num in initial_pos]
    
    # Run BFS to find the min number of moves
    while queue_pos < len(queue):
        # Get the current node
        node = queue[queue_pos]

        # Check if the current matches the target
        if check_state(node, target_state) == True:
            min_moves = node.num_of_moves
            break

        # Create a new node for each possible move and add it to the queue
        # Loop over each col and attempt to move the top most coin left and right
        for i in range(n):
            # Left
            if i - 1 >= 0 and len(node.state[i]) > 0 and (len(node.state[i - 1]) == 0 or node.state[i][0] < node.state[i - 1][0]):
                new_node = Node()
                new_node.state = [col for col in node.state]
                new_node.state[i - 1] = [new_node.state[i][0]] + new_node.state[i - 1]
                new_node.state[i] = new_node.state[i][1:]
                new_node.num_of_moves = node.num_of_moves + 1
                if check_for_dup(new_node, queue):
                    queue.append(new_node)

            # Right
            if i + 1 < n and len(node.state[i]) > 0 and (len(node.state[i + 1]) == 0 or node.state[i][0] < node.state[i + 1][0]):
                new_node = Node()
                new_node.state = [col for col in node.state]
                new_node.state[i + 1] = [new_node.state[i][0]] + new_node.state[i + 1]
                new_node.state[i] = new_node.state[i][1:]
                new_node.num_of_moves = node.num_of_moves + 1
                if check_for_dup(new_node, queue):
                    queue.append(new_node)

        # Get ready for the next iteration
        queue_pos += 1


    # Print the answer
    if min_moves == -1:
        print("IMPOSSIBLE")
    else:
        print(min_moves)
    























    
