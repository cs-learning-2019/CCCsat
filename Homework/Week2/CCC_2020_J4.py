# CCC 2020 J4 Cyclic Shifts
# Kavan Lam
# Oct 1, 2021

# First get the inputs
T = input()
S = input()

# Generate all the cyclic shifts of S and check if it is a substring in T
answer = "no"
for i in range(len(S)):
    if S in T:
        answer = "yes"
        break

    S = S[1:] + S[0]

print(answer)
    
