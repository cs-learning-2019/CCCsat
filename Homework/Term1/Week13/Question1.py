# Python CCC
# Question 1
# Kavan Lam
# Dec 29, 2021

def find_min_pair(list_of_num):
    # Create a data structure to store the number of times each number comes up
    num_freq = {}
    for i in range(0, 15001):
        num_freq[i] = 0

    # Fill in the number frequency map
    for num in list_of_num:
        num_freq[num] = num_freq[num] + 1


    # Loop over the keys of num_freq to find the pair that has the minimum difference
    num1 = -1
    num2 = -1
    min_diff = -1
    last_present_num = -1
    for key in range(0, 15001):
        # If there are duplicate numbers in the list then the answer is the duplicate number itself
        if num_freq[key] > 1:
            return "(" + str(key) + "," + str(key) + ")"

        if num_freq[key] == 1:
            if last_present_num == -1:
                last_present_num = key
            elif min_diff == -1 or abs(key - last_present_num) < min_diff:
                num1 = last_present_num
                num2 = key
                min_diff = abs(num2 - num1)
                last_present_num = key
            else:
                last_present_num = key

    return "(" + str(num1) + "," + str(num2) + ")"


print(find_min_pair([10, 20, 15, 22]))
