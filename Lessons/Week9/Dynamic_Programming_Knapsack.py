# Python CCC
# Dynamic Programming Knapsack problem
# Kavan Lam
# Nov 19, 2021

# PROBLEM DESCRIPTION
# Given weights and values of n items,
# put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack.
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

# KEY IDEAS
# 1) We need a recusive relationship...
#    We know that for each item we can either include it or not
#    So, break down the problem by the first i items
#    If we can not include item i then the answer is the same as if we just had the first i-1 items
#    We we can include item i then the answer is the max between including it and not including it
#
# 2) We need a DP array. In this case it will be 2D. index [i][j] tells you the max value
#    by using only the first i items with a bag capacity of j
#    If i == 0 or j == 0 then the max value is zero.
#    Since i == 0 means we have no items and j == 0 means we have no capacity


# SOLUTION
def knap_sack(values, weights, capacity):
    # Create the dynmaic programming array
    num_of_items = len(values)
    dp_array = [[0 for j in range(capacity + 1)] for i in range(num_of_items + 1)]

    # Fill in the values in the dp array
    for i in range(1, num_of_items + 1):
        for j in range(1, capacity + 1):
            # Either we can fit the ith item or not
            if weights[i - 1] <= j:
                dp_array[i][j] = max(dp_array[i - 1][j - weights[i - 1]] + values[i - 1], dp_array[i - 1][j])
            else:
                dp_array[i][j] = dp_array[i - 1][j]

    # Get and return the answer
    return dp_array[num_of_items][capacity]


item_values = [60, 100, 120]
item_weights = [10, 20, 30]
capacity = 50
print(knap_sack(item_values, item_weights, capacity)) # Should print 220

item_values = [50, 100, 150, 200]
item_weights = [8, 16, 32, 40]
capacity = 64
print(knap_sack(item_values, item_weights, capacity)) # Should print 350



