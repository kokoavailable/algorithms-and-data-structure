class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 0 2 1 1 0 2
        # 0 1 1 0 2 2
        # 0 0 1 1 2 2

        for i in range(n):
            for j in range(0, n - i - 1):
                curr = nums[j]
                fow = nums[j+1]
                if curr > fow:
                    nums[j] = fow
                    nums[j+1] = curr

        return nums