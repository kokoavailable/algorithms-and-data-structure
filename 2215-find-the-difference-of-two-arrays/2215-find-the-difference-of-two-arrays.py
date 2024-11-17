class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1, set2 = set(nums1), set(nums2)

        distinct1 = list(set1 - set2)
        distinct2 = list(set2 - set1)

        return [distinct1, distinct2]
        
        