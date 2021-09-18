# CCC 2010 J5 Knight Hop
# Kavan Lam
# Note that this solution is not the fastest but very simple

# Get the starting point (start = [int(num) for num in input().split()])
start = input().split()
start = (int(start[0]), int(start[1]))

# Get the target point
end = input().split()
end = (int(end[0]), int(end[1]))

# Use BFS to find the shortest distance to the target point
queue = [(start[0], start[1], 0)]  # First come first serve data structure
shortest_distance = 0

while (len(queue) > 0):
    # Extract the next triplet in the queue
    current = queue[0]
    queue = queue[1:]

    # Check if the current position is our target
    if (current[:2] == end):
        shortest_distance = current[2]
        break

    # Compute the new positions that we can travel to
    new_distance = current[2] + 1
    x = current[0]
    y = current[1]

    if x + 1 <= 8 and y + 2 <= 8:
        queue.append((x + 1, y + 2, new_distance))
        
    if x + 2 <= 8 and y + 1 <= 8:
        queue.append((x + 2, y + 1, new_distance))
        
    if x + 2 <= 8 and y - 1 >= 1:
        queue.append((x + 2, y - 1, new_distance))
        
    if x + 1 <= 8 and y - 2 >= 1:
        queue.append((x + 1, y - 2, new_distance))
        
    if x - 1 >= 1 and y - 2 >= 1:
        queue.append((x - 1, y - 2, new_distance))
        
    if x - 2 >= 1 and y - 1 >= 1:
        queue.append((x - 2, y - 1, new_distance))
        
    if x - 2 >= 1 and y + 1 <= 8:
        queue.append((x - 2, y + 1, new_distance))
        
    if x - 1 >= 1 and y + 2 <= 8:
        queue.append((x - 1, y + 2, new_distance))
    
# Print the answer
print(shortest_distance)
