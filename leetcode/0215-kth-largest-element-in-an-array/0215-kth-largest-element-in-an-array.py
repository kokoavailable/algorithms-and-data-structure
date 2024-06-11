import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        max_heap = [-num for num in nums]
        
        heapq.heapify(max_heap)
        
        for _ in range(k - 1):
            heapq.heappop(max_heap)
            
        return -heapq.heappop(max_heap)