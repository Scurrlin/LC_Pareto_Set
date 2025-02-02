class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Track visited cells to avoid re-processing
        visit = set()

        def dfs(r, c):

            # Base case: Out of bounds, water, or already visited
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            
            # Mark the cell as visited
            visit.add((r, c))

            # Recursively explore all 4 directions and sum up the island area
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        # Store the maximum island area
        area = 0

        # Iterate through every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):

                # Update max area for each new island
                area = max(area, dfs(r, c))

        # Return the largest island found        
        return area

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)