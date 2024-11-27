class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtracking(k: int, total: int, number:int, temp: List[int]):
            if total > n or k < 0:
                return
            
            if k == 0 and total == n:
                result.append(temp[:])
                
            for i in range(number + 1, 10):
                temp.append(i)
                backtracking(k - 1 , total + i, i, temp)
                temp.pop()
                
        backtracking(k, 0, 0, [])
                
        return result
                
            