from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count occurrences of each number (O(N))
        count = Counter(nums)

        # Get top k frequent elements (O(N log k))
        return [num for num, _ in count.most_common(k)]

# Time Complexity: O(N log K)
# Space Complexity: O(N)