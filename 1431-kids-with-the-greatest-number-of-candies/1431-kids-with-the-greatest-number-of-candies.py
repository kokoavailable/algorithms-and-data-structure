class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        max_candy = max(candies) - extraCandies
        
        ls = []
        
        for candy in candies:
            if candy >= max_candy:
                ls.append(True)
            else:
                ls.append(False)
            
        return ls