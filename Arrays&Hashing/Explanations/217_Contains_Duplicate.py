class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Sort the array (O(N log N))
        nums.sort()
        
        # Get the number of elements
        n = len(nums)

        # Iterate through sorted list
        for i in range(1, n):

            # Check for consecutive duplicates
            if nums[i] == nums[i - 1]:

                # Duplicate found
                return True
        
        # No duplicates found
        return False

# Time Complexity: O(N log N)
# Space Complexity: O(1)