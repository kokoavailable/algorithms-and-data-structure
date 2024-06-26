class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int,[i for i in str(int("".join(map(str, digits))) + 1)])