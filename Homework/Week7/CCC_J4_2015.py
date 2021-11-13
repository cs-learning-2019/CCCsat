# Python CCC
# J4 2015 Wait Time
# Kavan Lam
# Nov 6, 2021

# Get the first input
M = int(input())

# Prepare data structure to store the wait time across the friends
# Each key:value pair will have this format
# The key will be an integer representing the friend number
# The value will be a list [x, y] where x is the total wait time and y is whether or not the friend is waiting
# For example, {2:[15, True]} we have friend 2 who has waited 15 seconds so far and is currently waiting for a response
wait_times = {}

# Define a helper function to increase the wait times of all active friends by a given amount
def increase(time):
    for friend_num in wait_times:
        if wait_times[friend_num][1] == True:
            wait_times[friend_num][0] += time

# Process the remaining lines of input one by one
prev_command = ""
for i in range(M):
    entry = input().split(" ")
    entry[1] = int(entry[1])

    if entry[0] == "R":
        if prev_command != "W":
            increase(1)
        if entry[1] in wait_times:
            wait_times[entry[1]][1] = not wait_times[entry[1]][1]
        else:
            wait_times[entry[1]] = [0, True]
    elif entry[0] == "W":
        increase(entry[1])
    else:
        if prev_command != "W":
            increase(1)
        wait_times[entry[1]][1] = not wait_times[entry[1]][1]

    prev_command = entry[0]
          

# Print the answer
friend_numbers = list(wait_times.keys())
friend_numbers.sort()
for friend_number in friend_numbers:
    if wait_times[friend_number][1] == True:
        print(friend_number, -1)
    else:
        print(friend_number, wait_times[friend_number][0])



