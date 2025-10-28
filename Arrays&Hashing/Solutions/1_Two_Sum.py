class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in hashMap:
                return [hashMap[x], i]
            hashMap[num] = i

# Time Complexity: O(n)
# Space Complexity: O(n)