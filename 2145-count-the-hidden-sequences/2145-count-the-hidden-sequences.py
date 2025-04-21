class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_sum = 0
        max_sum = 0
        current = 0

        for diff in differences:
            current += diff
            min_sum = min(min_sum, current)
            max_sum = max(max_sum, current)
        
        min_start = lower - min_sum
        max_start = upper - max_sum

        if max_start < min_start:
            return 0
        else:
            return max_start - min_start + 1