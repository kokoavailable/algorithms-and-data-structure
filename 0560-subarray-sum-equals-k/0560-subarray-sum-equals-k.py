class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = 1  # 누적합 0이 처음에 1번 있다고 가정

        for num in nums:
            prefix_sum += num
            count += prefix_sum_map[prefix_sum - k]
            prefix_sum_map[prefix_sum] += 1

        return count