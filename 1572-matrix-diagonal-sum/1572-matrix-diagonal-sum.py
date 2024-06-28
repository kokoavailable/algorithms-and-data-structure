class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        total_sum = 0
        
        for i in range(len(mat)):
            left = i
            right = -1 - i
            
            total_sum += mat[i][left]
            
            if left != (n + right):
                total_sum += mat[i][right]
                
        return total_sum
        