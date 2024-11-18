class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ls_j = []
        pair_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                for k in range(len(grid)):
                    ls_j.append(grid[k][j])
                    
                if grid[i] == ls_j:
                    pair_count += 1
                    
                ls_j = []
                    
        return pair_count
            