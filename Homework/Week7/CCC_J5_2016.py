# Python CCC
# J5 2016 Tandem Bicycle
# Kavan Lam
# Nov 6, 2021

# First get the input
type_of_problem = input()
N = int(input())
dmo = [int(speed) for speed in input().split(" ")]
peg = [int(speed) for speed in input().split(" ")]

# Sort each of the list of speeds
dmo.sort()
peg.sort()

# If we want to max the total speed then reverse peg
if type_of_problem == "2":
    peg.reverse()

# For max we want to match all the slowest guys in dmo with the fastest guys from peg
    # This allows for the slow guys to get assisted by the fast guys so they don't slow down the pack
# For min we want to match all the slowest guys in dmo with the slowest guys from peg
    # This allows for the a lot of the fast guys to get wasted by putting them with other fast guys

# Find the total speed
total = 0
for index in range(N):
    total += max(dmo[index], peg[index])

print(total)
    
