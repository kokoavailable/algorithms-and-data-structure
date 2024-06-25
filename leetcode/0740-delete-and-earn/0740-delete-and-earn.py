class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_val = max(nums)
        count = [0] * (max_val + 1)
        
        for num in nums:
            count[num] += num
            
        dp = [0] * (max_val + 1)
        dp[0] = 0
        dp[1] = count[1]
        
        for i in range(2, max_val + 1):
            dp[i] = max(dp[i-1], dp[i-2] + count[i])
            
        return dp[max_val]