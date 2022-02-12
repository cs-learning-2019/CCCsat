# Python CCC
# Min Heap: Question 3
# Kavan Lam
# Feb 12, 2022

import heapq
from heapq import heappop

def heapSort(num_list):
    # Transform the input list into a min-heap
    heapq.heapify(num_list)

    sorted_list = []
    for i in range(len(num_list)):
        num = heappop(num_list)
        sorted_list.append(num)
 
    return sorted_list
 

num_list = [7, 4, 6, 3, 9, 1, 2, 20, 1]
print(heapSort(num_list))


