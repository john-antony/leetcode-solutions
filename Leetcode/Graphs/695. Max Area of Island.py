class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        maxislandarea = 0
    

        rowsLen, colsLen = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r not in range(rowsLen) or c not in range(colsLen) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        

        for r in range(rowsLen):
            for c in range(colsLen):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxislandarea = max(maxislandarea, dfs(r, c))
        
        return maxislandarea

