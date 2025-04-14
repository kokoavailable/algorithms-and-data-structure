class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) + 1): 
            for combo in combinations(nums, i):
                result.append(list(combo))
        return result


