# Get the input
num = int(input())

# Figure out the number of representations
if num > 5:
    num_of_rep = 1 + ((5 - (num - 5)) // 2)
else:
    num_of_rep = 1 + (num // 2)
    
# Print the answer
print(num_of_rep)
