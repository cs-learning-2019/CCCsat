# Python CCC
# TLE '16 Mock CCC S1: Writing the CCC
# Kavan Lam
# Oct 30, 2021

# Create data structures to help us
problem_type_to_positions = {}
problem_type_preference = []

# Now get the input and process it
T = int(input())
for i in range(T):
    problem_type_preference.append(input())

N = int(input())
for i in range(N):
    problem_type = input()
    if problem_type in problem_type_to_positions:
        problem_type_to_positions[problem_type].append(i + 1)
    else:
        problem_type_to_positions[problem_type] = [i + 1]

# print the answer
for problem_type in problem_type_preference:
    positions = problem_type_to_positions[problem_type]
    for pos in positions:
        print(pos)
