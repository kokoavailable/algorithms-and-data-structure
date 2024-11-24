class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        number = None
        
        for num in nums:
            if count == 0:
                number = num
                
            count += 1 if number == num else -1
            
        return number