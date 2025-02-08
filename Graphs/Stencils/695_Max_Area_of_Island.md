```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = l(g), l(g[0])
        v = s()

        d d(r, c):
            i (
                r < 0
                o r == R
                o c < 0
                o c == C
                o g[r][c] == 0
                o (r, c) i v
            ):
                r 0
            v.a((r, c))
            r 1 + d(r + 1, c) + d(r - 1, c) + d(r, c + 1) + d(r, c - 1)

        a = 0
        f r i r(R):
            f c i r(C):
                a = m(a, d(r, c))
        r a

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)
```