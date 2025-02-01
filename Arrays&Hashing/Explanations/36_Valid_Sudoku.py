class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b = board

        # Track numbers in each row, column, and 3x3 box
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                # Skip empty cells
                if b[r][c] == ".":
                    continue
                
                # Check if the number already exists in row, column, or 3x3 box
                if (
                    b[r][c] in rows[r]
                    or b[r][c] in cols[c]
                    or b[r][c] in squares[(r//3, c//3)]
                ):
                    # Duplicate found → Invalid board
                    return False
                
                # Store number in row, column, and 3x3 box
                rows[r].add(b[r][c])
                cols[c].add(b[r][c])
                squares[(r//3, c//3)].add(b[r][c])
        
        # No duplicates → Valid Sudoku board
        return True

# Time Complexity: O(1)
# Space Complexity: O(1)