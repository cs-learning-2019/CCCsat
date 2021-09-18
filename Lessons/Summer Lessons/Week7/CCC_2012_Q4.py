# CCC 2012 J4 Big Bang Secrets
# Kavan Lam

# First get the input
K = int(input())
word = input()

# Create a data structure to hold the alphabet in reverse order
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alpha.reverse()

# Create a helper function to decode the a single letter
def decode_letter(letter, index):
    global K
    global alpha

    # Compute the shift amount
    S = (3 * (index + 1)) + K

    # Apply the shift amount in the reverse alphabet to get the original letter
    new_letter = alpha[(alpha.index(letter) + S) % 26]

    return new_letter

# Decode the word
decoded_word = ""
for index in range(len(word)):
    decoded_word += decode_letter(word[index], index)

print(decoded_word)
