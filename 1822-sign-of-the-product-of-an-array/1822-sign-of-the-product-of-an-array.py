class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None
        
        if 0 in nums:
            return 0
        
        negative_cnt = 0
        
        for num in nums:
            if num < 0:
                negative_cnt += 1
                
        if negative_cnt % 2 == 0:
            return 1
        else:
            return -1
        