# Python CCC
# Question 7
# Kavan Lam
# Dec 29, 2021

import heapq
from heapq import heappop
 
# Function to find the k'th smallest element in a list using min-heap
# We assume that k < len(num_list)
def find_kth_smallest(num_list, k):
    # Transform the input list into a min-heap
    heapq.heapify(num_list)
 
    # Pop from min-heap exactly k-1 times
    # Doing so leaves the kth smallest number at the top of the min-heap
    for i in range(k - 1):
        heappop(num_list)
 
    # Return the root of min-heap
    return num_list[0]
 

num_list = [7, 4, 6, 3, 9, 1]
k = 3
print("k'th smallest element in the list is " + str(find_kth_smallest(num_list, k)))
