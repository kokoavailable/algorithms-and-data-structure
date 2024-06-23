class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 연속해서 선택하지 않되, 모든 합이 최대값이 되는 조합.
        # 모든 조합을 고려하되, 중복되지는 않게
        # 꼭 하나건너 하나 턴다고 최적은 아니다.. 유저는 각 집에서 선택의 기로에 놓인다.. 털거냐 안털거나.. 그리고 앞을 털었냐안털었냐
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
            
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[-1]