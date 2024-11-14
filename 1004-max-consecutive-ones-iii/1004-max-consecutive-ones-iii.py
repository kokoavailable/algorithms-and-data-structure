class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        max_len = 0
        zero_count = 0
        
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
                
            while zero_count > k:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
                
            max_len = max(max_len, j - i + 1)

        return max_len