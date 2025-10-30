class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        l, r = 0, len(n) - 1

        while l < r:
            total = n[l] + n[r]
            if total == target:
                return[l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1

# Time Complexity: O(N)
# Space Complexity: O(1)