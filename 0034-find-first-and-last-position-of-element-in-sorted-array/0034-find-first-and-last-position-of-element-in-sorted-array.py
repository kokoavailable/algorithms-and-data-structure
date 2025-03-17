from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            low, high = 0, len(nums) - 1
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    res = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return res
        
        def find_last():
            low, high = 0, len(nums) - 1
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    res = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return res
        
        first = find_first()
        if first == -1:
            return [-1, -1]
        last = find_last()
        return [first, last]