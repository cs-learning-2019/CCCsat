# CCC 2010 J4 Global Warming
# Kavan Lam

answers = []
while(True):
    # Get the input
    """
    temp = input().strip().split()
    for num in temp:
        num_seq.append(int(num))
    """
    num_seq = [int(num) for num in input().strip().split()]

    # Quit if input is zero
    if num_seq[0] == 0:
        break

    # Remove the first number
    num_seq = num_seq[1:]

    # Get the differences
    delta = []
    for index in range(1, len(num_seq)):
        delta.append(int(int(num_seq[index]) - int(num_seq[index - 1])))

    # Take care of the edge case where you are only given one temperature
    if (len(delta) == 0):
        answers.append(0)
        continue

    # Compute the length of the shortest temp cycle
    shortest_seq = [delta[0]]  # I called this the SRC in class
    current_seq = []

    for index in range(1, len(delta)):
        # Update current sequence
        current_seq.append(delta[index])

        # Check if current seq does not match the shortest seq
        if not(current_seq == shortest_seq[:len(current_seq)]):
           shortest_seq = delta[:index + 1]
           current_seq = []
            
        # Clear the current seq if it is full
        if (len(current_seq) >= len(shortest_seq)):
            current_seq = []
        
    # Print the length of the shortest temp cycle
    answers.append(len(shortest_seq))

for answer in answers:
    print(int(answer))


    
