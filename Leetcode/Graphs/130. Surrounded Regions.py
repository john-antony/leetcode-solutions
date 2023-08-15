class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # O(n * m)
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        # first pass to change all unsurrounded regions to a "T"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c)
        # Second pass to change all surrounded "O" into "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # Third pass to change all "T" back to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    

            