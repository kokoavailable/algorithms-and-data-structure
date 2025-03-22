class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n
        water = 0


        # preprocessing

        ## 1. left maxima
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        ## 2. right maxima
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i]) 

        ### final process
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water