class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        max_candy = max(candies)
        result = [(candy + extraCandies) >= max_candy for candy in candies]
        return result
