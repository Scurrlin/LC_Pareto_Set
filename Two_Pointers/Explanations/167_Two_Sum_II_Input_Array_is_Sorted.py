class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Alias for readability
        n, t = numbers, target

        # Left and right pointers
        l, r = 0, len(n) - 1

        while l < r:

            # Compute sum of two elements
            total = n[l] + n[r]

            if total == t:

                # Return 1-based indices
                return[l + 1, r + 1]
            elif total < t:

                # Increase sum by moving left pointer right
                l += 1
            else:

                # Decrease sum by moving right pointer left
                r -= 1

# Time Complexity: O(N)
# Space Complexity: O(1)