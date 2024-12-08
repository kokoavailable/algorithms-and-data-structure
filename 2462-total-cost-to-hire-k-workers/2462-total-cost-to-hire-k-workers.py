class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_heap = []
        right_heap = []

        for i in range(candidates):
            heapq.heappush(left_heap, (costs[i], i))

        for i in range(max(candidates, n - candidates), n):
            heapq.heappush(right_heap, (costs[i], i))

        total_cost = 0
        left_idx = candidates 
        right_idx = n - candidates - 1 
        
        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0][0] <= right_heap[0][0]):
                cost, idx = heapq.heappop(left_heap)
                total_cost += cost
                if left_idx <= right_idx:
                    heapq.heappush(left_heap, (costs[left_idx], left_idx))
                    left_idx += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total_cost += cost
                if right_idx >= left_idx:
                    heapq.heappush(right_heap, (costs[right_idx], right_idx))
                    right_idx -= 1

        return total_cost