class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum = 0
        result = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1

            result += (right - left + 1)

        return result