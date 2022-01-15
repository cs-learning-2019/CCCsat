# Python CCC
# Question 4
# Kavan Lam
# Dec 29, 2021

# This solution uses Kadane’s Algorithm which is O(n) (better than divide and conquer)
def find_max_subarray_sum(list_of_num):
    temp_max = 0
    abs_max = None

    for num in list_of_num:
        temp_max += num
        temp_max = max(temp_max, num)
        if abs_max is None:
            abs_max = temp_max
        abs_max = max(abs_max, temp_max)

    return abs_max
    

test_list1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test_list2 = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
test_list3 = [2, -4, 1, 9, -6, 7, -3]
print("The max subarray sum is " + str(find_max_subarray_sum(test_list3)))
