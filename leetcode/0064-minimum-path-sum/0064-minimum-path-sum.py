class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * n for _ in range(m)]  # 초기화를 0으로 변경
        
        dp[0][0] = grid[0][0]  # 시작점 초기화
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:  # 첫 번째 행 처리
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0 and i > 0:  # 첫 번째 열 처리
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif i > 0 and j > 0:  # 나머지 셀 처리
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])  
        
        return dp[m-1][n-1]