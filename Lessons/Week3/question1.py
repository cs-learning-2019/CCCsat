def question1(list_of_nums):
    for sublist in list_of_nums:
        for num in sublist:
            print(num)

def question1_alternative(list_of_nums):
    for main_index in range(len(list_of_nums)):
        for sub_index in range(len(list_of_nums[main_index])):
            print(list_of_nums[main_index][sub_index])

my_list = [[4, 5, 1], [0], [], [6, 1, 9, -1]]
question1_alternative(my_list)
