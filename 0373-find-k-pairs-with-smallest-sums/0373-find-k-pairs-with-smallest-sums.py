class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        heap = []
        visited = set()
        answer = []

        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        len1, len2 = len(nums1), len(nums2)

        while heap and len(answer) < k:
            current_sum, i, j = heapq.heappop(heap)
            answer.append([nums1[i], nums2[j]])

            # 다음 후보 (i+1, j) 처리
            if i + 1 < len1 and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))

            # 다음 후보 (i+1, j) 처리
            if j + 1 < len2 and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))

        return answer