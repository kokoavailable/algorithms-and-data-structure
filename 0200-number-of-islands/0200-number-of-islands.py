class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # 새로운 섬 발견
                    islands += 1
                    dfs(i, j)  # 연결된 모든 땅을 방문 처리
        return islands
