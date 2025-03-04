class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Initialize binary search bounds
        start, end = 0, len(nums) - 1

        # Track the minimum value 
        curr_min = float("inf")

        # Alias for readability
        n = nums
        
        while start < end:

            # Compute middle index
            m = start + (end - start)//2

            # Update minimum value
            curr_min = min(curr_min, n[m])

            # If mid element is greater than end, the min must be in the right half
            if n[m] > n[end]:

                # Shift right
                start = m + 1

            # Otherwise, the min is in the left half (including mid)    
            else:

                # Shift left
                end = m - 1 

        # Ensure min is updated        
        return min(curr_min, n[start])

# Time Complexity: O(log N)
# Space Complexity: O(1)