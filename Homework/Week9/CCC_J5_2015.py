# CCC J5 2015 Pie Day
# Nov 13, 2021

# Here is the dynamic programming solution

# First get the input
n = int(input())
k = int(input())

# Build the DP array
num_of_ways = []
for num_of_cakes in range(n + 1):
    num_of_ways.append([0 for num_of_people in range(k + 1)])

# If there is one person then the answer is always 1 no matter how many cakes
# Also if n = k then there is only one way as well
for num_of_cakes in range(0, n + 1):
    num_of_ways[num_of_cakes][1] = 1
    if num_of_cakes <= k and num_of_cakes > 0:
        num_of_ways[num_of_cakes][num_of_cakes] = 1
        

# Fill in the DP array 
for num_of_cakes in range(1, n + 1):
    for num_of_people in range(1, min(k, num_of_cakes) + 1):
        num_of_ways[num_of_cakes][num_of_people] = num_of_ways[num_of_cakes - 1][num_of_people - 1] + num_of_ways[num_of_cakes - num_of_people][num_of_people]


# Print the answer
print(num_of_ways[n][k])


# Below is the recursive solution that is slow 10/15 marks
"""
n = int(input())
k = int(input())

def num_of_ways(num_of_cakes, num_of_people):
    if num_of_cakes < num_of_people:
        return 0
    elif num_of_people == 1 or num_of_cakes == num_of_people:
        return 1
   
    return pie(num_of_cakes - 1, num_of_people - 1) + pie(num_of_cakes - num_of_people, num_of_people)

print(num_of_ways(n, k))
"""
