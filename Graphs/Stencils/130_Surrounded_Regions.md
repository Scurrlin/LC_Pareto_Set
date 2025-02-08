```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        b = b
        m, n = l(b), l(b[0])

        d d(x, y):
            b[x][y] = '#'
            f x, y i ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                i 0 <= x < m a 0 <= y < n a b[x][y] == 'O':
                    d(x, y)

        f i i r(m):
            i b[i][0] == 'O': d(i, 0)
            i b[i][n-1] == 'O': d(i, n-1)
        f j i r(n):
            i b[0][j] == 'O': d(0, j)
            i b[m-1][j] == 'O': d(m-1, j)

        f x i r(m):
            f y i r(n):
                i b[x][y] == 'O':
                    b[x][y] = 'X'
                e b[x][y] == '#':
                    b[x][y] = 'O'

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)
```