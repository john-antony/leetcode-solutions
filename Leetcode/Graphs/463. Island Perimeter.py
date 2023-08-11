class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # O(n * m) visits every cell once

        visited = set()

        def dfs(r, c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))

            perim = dfs(r, c + 1)
            perim += dfs(r + 1, c)
            perim += dfs(r, c - 1)
            perim += dfs(r - 1, c)
            return perim
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)

