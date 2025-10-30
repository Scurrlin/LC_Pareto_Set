class Solution:
    def solve(self, board: List[List[str]]) -> None:
        b = board
        m, n = len(b), len(b[0])
        
        def dfs(x, y):
            b[x][y] = '#'
            for x2, y2 in ( 
                (x + 1, y), (x - 1, y),
                (x, y + 1), (x, y - 1)):
                
                if (0 <= x2 < m 
                    and 0 <= y2 < n 
                    and b[x2][y2] == 'O'):
                    dfs(x2, y2)
        
        for i in range(m):
            if b[i][0] == 'O': dfs(i, 0)
            if b[i][n - 1] == 'O': dfs(i, n - 1)
        for j in range(n):
            if b[0][j] == 'O': dfs(0, j)
            if b[m - 1][j] == 'O': dfs(m - 1, j)
            
        for x in range(m):
            for y in range(n):
                if b[x][y] == 'O':
                    b[x][y] = 'X'
                elif b[x][y] == '#':
                    b[x][y] = 'O'

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)