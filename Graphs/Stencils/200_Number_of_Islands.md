```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        i n g:
            r 0
        r, c = l(g), l(g[0])
        i = 0
        
        d d(r, c):
            i n (0 <= r < r 
                a 0 <= c < c
                a g[r][c] == '1'):
                r
            
            g[r][c] = '0'
            d(r - 1, c)
            d(r + 1, c)
            d(r, c - 1)
            d(r, c + 1)
        
        f r i r(r):
            f c i r(c):
                i g[r][c] == '1':
                    d(r, c)
                    i += 1
        
        r i

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)
```