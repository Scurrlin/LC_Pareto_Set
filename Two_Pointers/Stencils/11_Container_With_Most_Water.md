```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, l(h) - 1
        m_a = 0
        h = h

        w l < r:
            a = m(h[l], h[r]) * (r - l)
            m_a = m(m_a, a)
            i h[l] < h[r]:
                l += 1
            e:
                r -= 1
        r m_a

# Time Complexity: O(N)
# Space Complexity: O(1)
```