from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.dq = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        count = 0
        self.dq.append(t)
        
#         for item in self.dq:
#             if t - 3000 <= item <= t:
#                 count += 1
#         return count

        # queue 자료구조에서 popleft 는 O(n)의 시간복잡도
        
        while self.dq[0] < t - 3000:
            self.dq.popleft()
        
        return len(self.dq)
    
        #[-2999,1]
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)