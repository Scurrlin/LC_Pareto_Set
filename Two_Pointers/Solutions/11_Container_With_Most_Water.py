class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        h = height

        while l < r:
            area = min(h[l], h[r]) * (r - l)
            max_area = max(max_area, area)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return max_area

# Time Complexity: O(N)
# Space Complexity: O(1)