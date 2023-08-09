class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Time complexity: O(n * m * dfs) dfs: called 4 times so 4^len(word)
        #                  O(n * m * 4^n)

        ROWS, COLS = len(board), len(board[0])

        path = set()

        def dfs(i, r, c):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
                    
            path.add((r,c))

            res = (dfs(i + 1, r + 1, c) or 
                    dfs(i + 1, r - 1, c) or 
                    dfs(i + 1, r, c + 1) or 
                    dfs(i + 1, r, c - 1))
            path.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False


