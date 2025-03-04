class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        n, t = nums, target

        while l <= r:
            m = l + ((r - l)//2)
            if n[m] > t:
                r = m - 1
            elif n[m] < t:
                l = m + 1
            else:
                return m
        return -1

# Time Complexity: O(log N)
# Space Complexity: O(1)