class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b = board
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if b[r][c] == ".":
                    continue
                
                if (
                    b[r][c] in rows[r]
                    or b[r][c] in cols[c]
                    or b[r][c] in squares[(r//3, c//3)]
                ):
                    return False
                
                rows[r].add(b[r][c])
                cols[c].add(b[r][c])
                squares[(r//3,c //3)].add(b[r][c])
        
        return True