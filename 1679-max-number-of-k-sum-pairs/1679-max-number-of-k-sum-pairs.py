class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        i, j = 0, len(nums) - 1
        nums.sort()
        
        while i < j:
            sum = nums[i] + nums[j]
            if sum == k:
                cnt += 1
                i += 1
                j -= 1
            elif sum < k:
                i += 1
            else:
                j -= 1
                
            
        return cnt