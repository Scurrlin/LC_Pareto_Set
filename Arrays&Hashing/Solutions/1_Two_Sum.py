class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in h_map:
                return [h_map[x], i]
            h_map[num] = i

# h_map = hash_map

# Time Complexity: O(n)
# Space Complexity: O(n)