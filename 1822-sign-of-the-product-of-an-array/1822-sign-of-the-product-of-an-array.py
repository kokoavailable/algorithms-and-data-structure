class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign = 1
        
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign = -sign
        
        return sign