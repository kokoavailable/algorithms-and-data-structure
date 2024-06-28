class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        current_max = 0
        for customer in accounts:
            current_max = max(current_max, sum(customer))
            
        return current_max