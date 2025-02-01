class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        while l <= r:

            # Find the middle index
            mid = (l + r) // 2
            if target == nums[mid]:

                # Target found, return index
                return mid

            # Determine if the left half is sorted
            if nums[l] <= nums[mid]:

                # Target is outside the sorted left half, search right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1

                # Target is inside the sorted left half, search left    
                else:
                    r = mid - 1
            else:

                # Target is outside the sorted right half, search left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1

                # Target is inside the sorted right half, search right
                else:
                    l = mid + 1
        
        # Target not found
        return -1

# Time Complexity: O(log N)
# Space Complexity: O(1)