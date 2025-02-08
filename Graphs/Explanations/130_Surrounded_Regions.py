class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # Alias for readability
        b = board

        # Get board dimensions
        m, n = len(b), len(b[0])

        # Perform DFS to mark connected 'O's from the border
        def dfs(x, y):

            # Temporarily mark as visited
            b[x][y] = '#'

            # Explore neighbors
            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= x2 < m and 0 <= y2 < n and b[x2][y2] == 'O':
                    dfs(x2, y2)

        # Step 1: Capture all 'O's on the border and their connected components
        for i in range(m):

            # Left border
            if b[i][0] == 'O': dfs(i, 0)

            # Right border
            if b[i][n-1] == 'O': dfs(i, n-1)
        for j in range(n):

            # Top border
            if b[0][j] == 'O': dfs(0, j)

            # Bottom border
            if b[m-1][j] == 'O': dfs(m-1, j)

        # Step 2: Convert all unmarked 'O's to 'X' and restore '#' back to 'O'
        for x in range(m):
            for y in range(n):

                # Flip enclosed '0' to 'X'
                if b[x][y] == 'O':
                    b[x][y] = 'X'

                # Restore non-flipped 'O's    
                elif b[x][y] == '#':
                    b[x][y] = 'O'

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)