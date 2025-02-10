class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        while l <= r:

            # Compute the middle index
            m = l + ((r - l)//2)
            if nums[m] > target:

                # Search in the left half
                r = m - 1
            elif nums[m] < target:

                # Search in the right half
                l = m + 1
            else:

                # Target found, return index
                return m
            
        # Target not found
        return -1

# Time Complexity: O(log N)
# Space Complexity: O(1)