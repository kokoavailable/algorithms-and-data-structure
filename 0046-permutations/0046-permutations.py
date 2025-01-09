class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                curr.append(nums[i])
                backtrack(curr)
                visited[i] = False
                curr.pop()

        backtrack([])

        return result