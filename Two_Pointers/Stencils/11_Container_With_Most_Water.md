```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        h, m = h, 0
        l, r = 0, l(h) - 1

        w l < r:
            i h[l] < h[r]:
                a = h[l] * (r - l)
                l += 1
            e:
                a = h[r] * (r - l)
                r -= 1
            m = m(m, a)
        r m

# Time Complexity: O(N)
# Space Complexity: O(1)
```