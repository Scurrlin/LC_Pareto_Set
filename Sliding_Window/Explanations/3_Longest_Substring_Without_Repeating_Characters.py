class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # HashSet to store unique characters in the current window
        charSet = set()

        # Left pointer of the sliding window
        l = 0

        # Stores the maximum length of a unique substring
        res = 0

        # Right pointer expands the window
        for r in range(len(s)):

            # If duplicate found, shrink window from left
            while s[r] in charSet:
                charSet.remove(s[l])

                # Move left pointer forward
                l += 1

            # Add current character to the set    
            charSet.add(s[r])

            # Update max length found
            res = max(res, r - l + 1)

        # Return the length of the longest unique substring
        return res

# Time Complexity: O(N)
# Space Complexity: O(1)