# Python CCC
# Max Heap Data Structure
# Kavan Lam
# Feb 12, 2022

class MaxHeap:
    def __init__(self, array):
        self.elements = []
        self.heapSize = 0
        self.buildHeap(array)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return (i * 2) + 1

    def right(self, i):
        return (i * 2) + 2

    def swap(self, x, y):
        temp = self.elements[x]
        self.elements[x] = self.elements[y]
        self.elements[y] = temp

    def buildHeap(self, array):
        n = len(array)
        self.elements = array
        self.heapSize = n
        for i in range(n // 2 - 1, -1, -1):
            self.maxHeapify(i)

    def maxHeapify(self, i):
        leftIndex = self.left(i)
        rightIndex = self.right(i)
        largest = i

        if leftIndex < self.heapSize and self.elements[leftIndex] > self.elements[largest]:
            largest = leftIndex
        
        if rightIndex < self.heapSize and self.elements[rightIndex] > self.elements[largest]:
            largest = rightIndex

        if largest != i:
            self.swap(i, largest)
            self.maxHeapify(largest)

    def extractMax(self):
        largest = self.elements[0]
        self.heapSize -= 1
        self.elements[0] = self.elements[-1]
        self.elements = self.elements[:-1]
        self.maxHeapify(0)

        return largest

    def increaseElement(self, i, newValue):
        if newValue < self.elements[i]:
            return

        self.elements[i] = newValue
        while i > 0 and self.elements[self.parent(i)] < self.elements[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def insertElement(self, element):
        self.heapSize += 1
        self.elements.append(element)
        self.increaseElement(len(self.elements) - 1, element)
    

h = MaxHeap([2, 5, 1, 8, 4, 0, 12, 10, 3])
print(h.elements)
h.insertElement(11)
print(h.elements)
h.extractMax()
print(h.elements)
        
        
    
