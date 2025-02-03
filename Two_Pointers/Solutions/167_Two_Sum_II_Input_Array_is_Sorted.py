class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n, t = numbers, target
        l, r = 0, len(n) - 1

        while l < r:
            total = n[l] + n[r]

            if total == t:
                return[l + 1, r + 1]
            elif total > t:
                r -= 1
            else:
                l += 1

# Time Complexity: O(N)
# Space Complexity: O(1)