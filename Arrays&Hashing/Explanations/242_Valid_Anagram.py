class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):

            # If lengths differ, they can't be anagrams
            return False
        
        # Sort both strings and compare
        return sorted(s) == sorted(t)

# Time Complexity: O(N)
# Space Complexity: O(N)