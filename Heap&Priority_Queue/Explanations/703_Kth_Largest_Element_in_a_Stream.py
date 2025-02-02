class KthLargest:
    def __init__(self, k: int, nums: List[int]):

        # Store elements in a min-heap
        self.minHeap, self.k = nums, k

        # Convert nums into a heap (O(N))
        heapq.heapify(self.minHeap)

        # Maintain only the k largest elements in the heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:

        # Add new value
        heapq.heappush(self.minHeap, val)

        # If heap exceeds k elements, remove the smallest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Root of the heap is the k-th largest element    
        return self.minHeap[0]

# Time Complexity: O(N log N)
# Space Complexity: O(K)