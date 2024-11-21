class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] == 0:
                            perimeter += 1

        return perimeter