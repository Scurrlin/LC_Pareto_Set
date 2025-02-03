class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Store the filtered alphanumeric characters
        new = ''
        for a in s:

            # Check if character is alphanumeric
            if a.isalpha() or a.isdigit():

                # Convert to lowercase and add to string
                new += a.lower()

        # Check if the string is the same reversed
        return (new == new[::-1])

# Time Complexity: O(N)
# Space Complexity: O(N)