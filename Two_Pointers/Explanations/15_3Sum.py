class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Store unique triplets
        res = []
        n = nums

        # Sort the array (O(N log N))
        n.sort()

        for i in range(len(n)):

            # Skip duplicate elements
            if i > 0 and n[i] == n[i - 1]:
                continue
            
            # Two-pointer setup
            j = i + 1
            k = len(n) - 1

            while j < k:

                # Compute sum of triplet
                total = n[i] + n[j] + n[k]

                if total < 0:

                    # Increase sum by moving left pointer right
                    j += 1
                elif total > 0:

                    # Reduce sum by moving right pointer left
                    k -= 1
                else:

                    # Found a valid triplet
                    res.append([n[i], n[j], n[k]])

                    # Move left pointer forward
                    j += 1

                    # Skip duplicate values
                    while n[j] == n[j - 1] and j < k:
                        j += 1
        
        # Return all unique triplets
        return res

# Time Complexity: O(N^2)
# Space Complexity: O(N)