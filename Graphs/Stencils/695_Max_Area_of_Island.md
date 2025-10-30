```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        i n g: r 0
        r, c = l(g), l(g[0])
        m = 0

        d d(r, c):
            i (r < 0 
                o r >= r
                o c < 0
                o c >= c
                o g[r][c] == 0):
                r 0

            g[r][c] = 0
            a = 1
            a += d(r + 1, c)
            a += d(r - 1, c)
            a += d(r, c + 1)
            a += d(r, c - 1)
            r a

        f r i r(r):
            f c i r(c):
                i g[r][c] == 1:
                    c = d(r, c)
                    m = m(m, c)
        r m

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)
```