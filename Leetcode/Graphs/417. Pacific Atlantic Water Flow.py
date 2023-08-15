class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return [[]]
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or prevHeight > heights[r][c]:
                return
            

            visited.add((r, c))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
            
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res


