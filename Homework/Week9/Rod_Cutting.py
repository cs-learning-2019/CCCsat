# Python CCC
# Week 9 HW Rod Cutting Problem Solution
# Kavan Lam
# Nov 27, 2021

"""
PLEASE REFER TO THIS WEBSITE FOR MORE DETAILS ON THE PROBLEM
https://www.techiedelight.com/rod-cutting/

Problem Description:
Given a rod of length n and a list of rod prices of length i, where 1 <= i <= n,
find the optimal way to cut the rod into smaller rods to maximize profit.
"""

# Find the recursive relationship
"""
The max value of a rod of length n is simply the max between
not splitting at all (the value is the simply the value of a rod of length n)
or splitting it into pieces.

If the max comes from splitting then we know that at least one of the splits
of length n - 1 must be part of the optimal splitting. We don't know which one it is
so we need to consider all of them and take the max.

In other words, the recursive relationship is as follows...
max value of n = MAX (value of n, MAX (value of 1 + max value of n - 1, ..., value of n - 1 + max value of 1 ))

This looks confusing but really we are simply finding the max between all the options for splitting
and the options are from 1 to n - 1
"""

# What is the DP array going to look like
"""
max_value = [1D list of nums]

max_value[i] represents the max value we can get from a rod of length i

we know that...
max_value[i] = MAX(max_value[i], MAX(value(1) + max_value[i - 1], ... , value(i - 1) + max_value[1]))
"""

# If we tried to use a 2D list like in the knapsack problem that would not
# work since we can use the same cut many times. In the knapsack problem
# each item could only be taken once.

# Code the solution
def rod_max_value(value, n):
    # Setup DP array and value list
    max_value = [0] * (n + 1)
    value = [0] + value

    # Fill in the DP array
    for rod_length in range(1, n + 1):
        for split_length in range(1, rod_length + 1):
            max_value[rod_length] = max(max_value[rod_length], value[split_length] + max_value[rod_length - split_length])

    # Return the answer
    return max_value[n]
    
value = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(value)
print('Max value is', rod_max_value(value, n))








