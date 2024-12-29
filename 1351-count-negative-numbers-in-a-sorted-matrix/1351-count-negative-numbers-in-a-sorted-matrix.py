class Solution(object):
    def countNegatives(self, grid):
        def binarySearch(row):
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid - 1  # 음수가 시작되는 더 왼쪽을 탐색
                else:
                    left = mid + 1  # 음수가 아닌 경우 더 오른쪽을 탐색
            return len(row) - left  # 음수가 시작되는 위치부터 끝까지의 개수

        count = 0
        for row in grid:
            count += binarySearch(row)  # 각 행에 대해 이진 탐색 수행
        return count