class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert list to a set for O(1) lookups
        n_set = set(nums)

        # Tracks longest consecutive sequence
        longest = 0

        for n in n_set:

            # Check if 'n' is the start of a sequence
            if (n - 1) not in n_set:

                # Initialize sequence length
                length = 1

                # Expand sequence if next number exists
                while (n + length) in n_set:
                    length += 1

                # Update longest sequence    
                longest = max(length, longest)

        # Return the length of the longest consecutive sequence        
        return longest

# Time Complexity: O(N)
# Space Complexity: O(N)