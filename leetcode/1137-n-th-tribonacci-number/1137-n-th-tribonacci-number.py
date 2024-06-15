class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        def tribo_memo(n, memo={}):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            elif n == 2:
                return 1
            memo[n] = tribo_memo(n - 1, memo) + tribo_memo(n - 2, memo) + tribo_memo(n - 3, memo)
            return memo[n]
            
        return tribo_memo(n)
            