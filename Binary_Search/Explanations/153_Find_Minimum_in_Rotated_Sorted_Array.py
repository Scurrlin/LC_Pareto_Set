class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Initialize binary search bounds
        start, end = 0, len(nums) - 1

        # Track the minimum value 
        curr_min = float("inf")
        
        while start  <  end :

            # Compute middle index
            mid = start + (end - start ) // 2

            # Update minimum value
            curr_min = min(curr_min, nums[mid])

            # If mid element is greater than end, the min must be in the right half
            if nums[mid] > nums[end]:

                # Shift right
                start = mid + 1

            # Otherwise, the min is in the left half (including mid)    
            else:

                # Shift left
                end = mid - 1 

        # Ensure min is updated        
        return min(curr_min, nums[start])

# Time Complexity: O(log N)
# Space Complexity: O(1)