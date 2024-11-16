class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, zero_count, max_len = 0, 0, 0
        
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
            
            while 1 < zero_count:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
                
                
            max_len = max(max_len, j - i + 1)
            
        return max_len - 1
            