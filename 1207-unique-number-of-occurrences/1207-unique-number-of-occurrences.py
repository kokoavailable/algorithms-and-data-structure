from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnter = Counter(arr)
        return len(cnter) == len(set(cnter.values()))