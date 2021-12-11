# Python CCC
# Finding a peak element in a list of numbers
# Credit to https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

# We can do the simple method of looping over the whole list
def find_a_peak(nums):
    for index in range(len(nums)):
        left_num = None
        if index - 1 >= 0:
            left_num = nums[index - 1]

        right_num = None
        if index + 1 < len(nums):
            right_num = nums[index + 1]  
       
        if (left_num is None or nums[index] >= left_num) and (right_num is None or nums[index] >= right_num):
            return nums[index]


# We can actually make this faster by using a divide and conquer method
# Lets take a look at the website for the code (I am too lazy to type it out)


test_list = [1, 3, 20, 4, 1, 0]
print("The number: " + str(find_a_peak(test_list)) + " is a peak")
    
