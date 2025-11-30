class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        extended = heights + [0]

        for i, h in enumerate(extended):
            while stack and extended[stack[-1]] > h:
                height = extended[stack.pop()]

                left = stack[-1] if stack else -1
                right = i

                width = right - left - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area