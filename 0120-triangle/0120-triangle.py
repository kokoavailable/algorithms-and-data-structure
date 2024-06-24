class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        
        memo = {}
        
        def helper(row, col):
            if row == len(triangle):
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            left = helper(row + 1, col)
            right = helper(row + 1, col + 1)
            
            memo[(row, col)] = triangle[row][col] + min(left, right)
            
            return memo[(row, col)]
    
        return helper(0, 0)