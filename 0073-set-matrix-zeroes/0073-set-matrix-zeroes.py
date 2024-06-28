class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None
        
        m = len(matrix[0])
        n = len(matrix)
        
        suspects = []
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    suspects.append((i, j))
        
        for suspect in suspects:
            x, y = suspect
            for i in range(m):
                matrix[x][i] = 0
            for i in range(n):
                matrix[i][y] = 0
                
        return matrix