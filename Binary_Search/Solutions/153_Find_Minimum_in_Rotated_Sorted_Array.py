class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1 
        curr_min = float("inf")
        n = nums

        while start < end :
            m = start + (end - start)//2
            curr_min = min(curr_min, n[m])
            if n[m] > n[end]:
                start = m + 1
            else:
                end = m - 1
        return min(curr_min, n[start])

# Time Complexity: O(log N)
# Space Complexity: O(1)