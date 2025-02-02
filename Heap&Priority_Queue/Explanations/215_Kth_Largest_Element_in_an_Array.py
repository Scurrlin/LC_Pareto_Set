class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Step 1: Initialize a min-heap with the first k elements
        heap = nums[:k]

        # Step 2: Convert the list into a min-heap (O(k) time)
        heapq.heapify(heap)
        
        # Step 3: Iterate through the remaining elements
        for num in nums[k:]:

            # If the current number is larger than the heap's root
            if num > heap[0]:

                # Remove the smallest element
                heapq.heappop(heap)

                # Insert the new number into the heap
                heapq.heappush(heap, num)
        
        # Step 4: Return the root of the min-heap (k-th largest element)
        return heap[0]

# Time Complexity: O(N log K)
# Space Complexity: O(K)