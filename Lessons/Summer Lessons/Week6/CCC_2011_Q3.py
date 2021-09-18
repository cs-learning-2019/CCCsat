# CCC 2011 J3 Sumac Sequences
# Kavan Lam

# Get the input (first two num in the seq)
t1 = int(input())
t2 = int(input())

# The sequence is at least length two since we are given the first two numbers.
seq_length = 2

# Compute the numbers in the seq and keep track of the length
while (t2 <= t1):
    seq_length += 1
    new_seq_num = t1 - t2
    t1 = t2
    t2 = new_seq_num

# Print the answer to the question
print(seq_length)
