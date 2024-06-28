class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        answer = []
        m = len(matrix)
        n = len(matrix[0])
        
        top, bottom, left, right = 0, m - 1, 0, n - 1

        while top <= bottom and left <= right:        
            for i in range(left, right + 1):
                 answer. append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    answer.append(matrix[bottom][i])       
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    answer.append(matrix[i][left])
                left += 1
                
        return answer