class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            
            for pile in piles:
                cnt += (pile + mid -1) // mid
                if cnt > h:
                    break
                
            if cnt > h:
                left = mid + 1
            else:
                right = mid

        return left
                    
                