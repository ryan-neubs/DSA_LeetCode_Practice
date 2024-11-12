class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        n = len(self.heap)
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        self.swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self.heapify_down(0)
        return item

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)
    

class MaxHeap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return i * 2 + 1
    
    def right_child(self, i):
        return i * 2 + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent[i])
            i = self.parent[i]

    def heapify_down(self, i):
        n = len(self.heap)
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        
        self.swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self.heapify_down(0)
        return item
    
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def size(self):
        return len(self.heap)