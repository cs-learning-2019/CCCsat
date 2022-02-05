# Python CCC
# Question 5
# Kavan Lam
# Dec 29, 2021

# We will use DP to solve this problem
def find_max_profit(rod_length):
    # Hard code some base cases
    if rod_length <= 0:
        return 0
    elif rod_length == 1:
        return 1
    elif rod_length == 2:
        return 2
    
    # First create the DP array to store intermediate results
    # T[i] = x means a rod of length i will have a max profit of x
    T = []
    for length in range(rod_length + 1):
        T.append(-1)

    # The max profit for a rod of length 0 or 1 or 2 is easy and these will be our base cases
    T[0] = 0
    T[1] = 1
    T[2] = 2

    # Iterate over the possible rod lengths and fill in the DP array
    for i in range(3, rod_length + 1):
        # Iterate over all the possible cuts that I can make and get the max
        T[i] = i  # We start it off with the case where we don't cut it at all
        for cut_length in range(1, i):
            T[i] = max(T[i], cut_length * T[i - cut_length])

    # Look into the DP array and extract the answer
    return T[rod_length]
    

rod_length = 15
print("The max profit is " + str(find_max_profit(rod_length)))
