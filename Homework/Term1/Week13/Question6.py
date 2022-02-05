# Python CCC
# Question 6
# Kavan Lam
# Dec 29, 2021

# The recursive relationship is as follows
# Let T[n] be the number of target binary strings of length n
# Suppose we have n bits
# The nth bit can either be a 0 or 1 (so we break this down into two cases)
# Case 1 If the nth bit is 0: In this case there are no issues since using a zero will not
# result in consecutive 1's so this leads to T[n-1] possibilities
# Case 2 If the nth bit is 1: In this case we can only use a 1 if the n-1th bit is also not a 1
# so it comes down to how many target binary string of length n-1 are there that do not end in 1.
# Well... that is the same as the number of target binary strings of length n-2 since we take any of
# those and append a 0 giving a target binary string of length n-1 that does not end in 1.
# Adding the two cases together results in T[n] = T[n - 1] + T[n - 2]

def find_num_target_binary_strings(length):
    # Hard code base cases
    if length <= 0:
        return 1
    elif length == 1:
        return 2

    # Set up the DP array
    T = []
    for n in range(length + 1):
        T.append(None)

    # Fill in the base cases
    T[0] = 1  # A binary string of length 0 has 1 way to have no consecutive 1's (simply nothing)
    T[1] = 2

    # Fill in the DP array
    for n in range(2, length + 1):
        T[n] = T[n - 1] + T[n - 2]

    # Extract answer from DP array
    return T[length]


length = 5
print("The number of target binary strings is " + str(find_num_target_binary_strings(length)))
