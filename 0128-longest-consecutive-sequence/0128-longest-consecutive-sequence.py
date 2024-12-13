class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        # Step 2: Set 순회
        for num in num_set:
            # 현재 숫자가 시퀀스 시작점인지 확인
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 연속된 숫자 찾기
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # 최대 길이 업데이트
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
    
        nums_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num - 1 in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(logest_streak, current_streak)