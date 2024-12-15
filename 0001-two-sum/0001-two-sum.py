class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[num] = i
        