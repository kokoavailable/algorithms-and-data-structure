class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_counter = Counter(tuple(row) for row in grid)
        col_counter = Counter(tuple(grid[i][j] for i in range(len(grid))) for j in range(len(grid)))
        
        
        return sum(row_counter[key] * col_counter[key] for key in row_counter)
            