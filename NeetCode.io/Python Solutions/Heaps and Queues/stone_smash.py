import heapq

def lastStoneWeight(stones):
    max_heap = [-stone for stone in stones] # manipulating the minheap by inverting all values
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        stone1 = -heapq.heappop(max_heap)
        stone2 = -heapq.heappop(max_heap)
        smash = stone1 - stone2
        if smash != 0:
            max_heap.append(-smash)
            heapq.heapify(max_heap)

    if max_heap:
        return -max_heap[0]
    return 0


print(lastStoneWeight([6,6,6,6]))