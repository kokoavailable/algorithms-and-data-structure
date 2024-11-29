class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = [[1] * i for i in range(1, numRows + 1)]
        
        print(result)
        
        for i in range(numRows):
            for j in range(len(result[i])):
                if j == 0 or j == len(result[i]) - 1:
                    continue
                    
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                
        return result
            