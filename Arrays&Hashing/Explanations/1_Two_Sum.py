class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Store seen numbers and their indices
        h_map = {}

        # Calculate complement
        for i, num in enumerate(nums):
            x = target - num

            # If complement exists, return indices
            if x in h_map:
                return [h_map[x], i]
            
            # Store current number's index
            h_map[num] = i

# h_map = hash_map

# Time Complexity: O(N)
# Space Complexity: O(N)