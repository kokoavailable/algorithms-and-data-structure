from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        return len(freq) == len(set(freq.values()))