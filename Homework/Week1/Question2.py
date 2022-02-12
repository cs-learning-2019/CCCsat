# Python CCC
# Min Heap: Question 2
# Kavan Lam
# Feb 12, 2022

def isMinHeap(array):
    # Just loop through the array from left to right and ensure
    # that for each element, the left and right neighbours are bigger
    for i in range(len(array)):
        # Check left
        leftIndex = (i * 2) + 1
        if leftIndex < len(array):
            if (array[i] > array[leftIndex]):
                return False

        # Check right
        rightIndex = (i * 2) + 2
        if rightIndex < len(array):
            if (array[i] > array[rightIndex]):
                return False


    # If we get here then we have a min heap
    return True


print(isMinHeap([10, 5, 2, 1, 0, 11, 12]))
print(isMinHeap([0, 3, 1, 5, 4, 2, 12, 10, 8]))
print(isMinHeap([-100, -1, 1, 5, 0, 2, 12, 10, 8, 3]))
