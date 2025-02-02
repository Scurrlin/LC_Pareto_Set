class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Convert to negative values to simulate max-heap
        stones = [-s for s in stones]

        # Heapify in O(N) time to maintain heap structure
        heapq.heapify(stones)

        while len(stones) > 1:

            # Largest stone (negated)
            first = heapq.heappop(stones)

            # Second largest stone (negated)
            second = heapq.heappop(stones)

            # If they are not equal, push the difference
            if second > first:

                # Push back the remaining weight
                heapq.heappush(stones, first - second)

        # Ensure there is at least one element to return
        stones.append(0)

        # Return absolute value of the last stone
        return abs(stones[0])

# Time Complexity: O(N log N)
# Space Complexity: O(N)