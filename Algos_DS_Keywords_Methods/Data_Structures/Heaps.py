# Heaps
# =====
# A heap is a special tree-based data structure that satisfies the heap
# property. In a max heap, for any given node, the value of the node is greater
# than or equal to the values of its children, and the highest value is at the
# root.

import heapq

min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
print(heapq.heappop(min_heap))  # Output: 1