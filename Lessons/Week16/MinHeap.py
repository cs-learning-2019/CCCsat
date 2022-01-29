# Python CCC
# Min Heap Data Structure
# Kavan Lam
# Jan 29, 2022

class MinHeap:
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
            self.minHeapify(i)

    def minHeapify(self, i):
        leftIndex = self.left(i)
        rightIndex = self.right(i)
        smallest = i

        if leftIndex < self.heapSize and self.elements[leftIndex] < self.elements[smallest]:
            smallest = leftIndex
        
        if rightIndex < self.heapSize and self.elements[rightIndex] < self.elements[smallest]:
            smallest = rightIndex

        if smallest != i:
            self.swap(i, smallest)
            self.minHeapify(smallest)

    def extractMin(self):
        smallest = self.elements[0]
        self.heapSize -= 1
        self.elements[0] = self.elements[-1]
        self.elements = self.elements[:-1]
        self.minHeapify(0)

        return smallest

    def decreaseElement(self, i, newValue):
        if newValue > self.elements[i]:
            return

        self.elements[i] = newValue
        while i > 0 and self.elements[self.parent(i)] > self.elements[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def insertElement(self, element):
        self.heapSize += 1
        self.elements.append(element)
        self.decreaseElement(len(self.elements) - 1, element)
    

#h = MinHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 10])
h = MinHeap([2, 5, 1, 8, 4, 0, 12, 10, 3])
print(h.elements)
h.insertElement(-1)
h.decreaseElement(0, 10)
h.decreaseElement(len(h.elements) - 1, -100)
print(h.elements)
        
        
    
