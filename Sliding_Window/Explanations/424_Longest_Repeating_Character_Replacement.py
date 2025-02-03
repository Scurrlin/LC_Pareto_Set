class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Dictionary to store character frequencies
        count = {}
        
        # Left pointer of the sliding window
        l = 0

        # Maximum frequency of any character in the window
        maxf = 0

        # Right pointer expands the window
        for r in range(len(s)):

            # Update frequency map
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update max frequency
            maxf = max(maxf, count[s[r]])

            # If more than `k` characters need to be replaced, shrink window
            if (r - l + 1) - maxf > k:

                # Reduce count of leftmost character
                count[s[l]] -= 1

                # Move left pointer forward
                l += 1

        # Return the maximum window size found
        return (r - l + 1)

# Time Complexity: O(N)
# Space Complexity: O(1)