class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Left and right pointers
        l, r = 0, len(height) - 1

        # Store maximum area found
        max_area = 0
        h = height

        while l < r:

            # Compute area
            area = min(h[l], h[r]) * (r - l)
            
            # Update max area
            max_area = max(max_area, area)

            # Move the pointer with the smaller height
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        
        # Return the largest area found
        return max_area

# Time Complexity: O(N)
# Space Complexity: O(1)