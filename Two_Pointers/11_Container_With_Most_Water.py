class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        h = height
        L = 0
        R = len(height) - 1

        while L < R:
            area = min(h[L], h[R]) * (R - L)
            max_area = max(max_area, area)

            if h[L] < h[R]:
                L += 1
            else:
                R -= 1
        
        return max_area