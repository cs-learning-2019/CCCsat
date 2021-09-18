# CCC 2011 J4 Boring Business
# Kavan Lam
# Note that this solution is not very efficient but I did it this way so
# you guys will have an easier time understanding.

# Setup the initial state
current_pos = (0, -1)
initial_moves = ["d 2", "r 3", "d 2", "r 2", "u 2", "r 2", "d 4", "l 8", "u 2"]
visited_pos = {(0, -1)}  # We will use a set and not a list for faster look up
danger = False

# Define a helper function to process a drill move and detect collisions
# Note this function will use visited_pos, current_pos and danger which are in the global scope
def move_drill(direction, steps):
    global visited_pos
    global current_pos
    global danger
    
    temp = current_pos
    
    if (direction == "d"):
        for step in range(steps):
            temp = (temp[0], temp[1] - 1)
            if (temp in visited_pos):
                danger = True
                break
            else:
                visited_pos.add(temp)
        current_pos = (current_pos[0], current_pos[1] - steps)
        
    elif (direction == "u"):
        for step in range(steps):
            temp = (temp[0], temp[1] + 1)
            if (temp in visited_pos):
                danger = True
                break
            else:
                visited_pos.add(temp)
        current_pos = (current_pos[0], current_pos[1] + steps)
        
    elif (direction == "l"):
        for step in range(steps):
            temp = (temp[0] - 1, temp[1])
            if (temp in visited_pos):
                danger = True
                break
            else:
                visited_pos.add(temp)
        current_pos = (current_pos[0] - steps, current_pos[1])
        
    elif (direction == "r"):
        for step in range(steps):
            temp = (temp[0] + 1, temp[1])
            if (temp in visited_pos):
                danger = True
                break
            else:
                visited_pos.add(temp)
        current_pos = (current_pos[0] + steps, current_pos[1])
    
# Process the initial moves
for move in initial_moves:
    direction = move.split()[0]
    steps = int(move.split()[1])
    move_drill(direction, steps)

# Process the remaining moves from input
move = input()
while (move[0] != "q" and danger == False):
    # Move the drill
    direction = move.split()[0]
    steps = int(move.split()[1])
    move_drill(direction, steps)

    # Print out the new position and if we are in danger or not
    if (danger == True):
        msg = "DANGER"
    else:
        msg = "safe"
    print(str(current_pos[0]) + " " + str(current_pos[1]) + " " + msg)

    # Get the next input if we are not in danger
    if (danger == False):
        move = input()


    
