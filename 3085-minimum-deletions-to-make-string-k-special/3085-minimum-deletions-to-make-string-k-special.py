class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        max_freq = max(freq)
        min_deletions = float('inf')

        for M in range(1, max_freq + 1):
            deletions = 0
            for c in freq:
                if c > M:
                    deletions += c - M
                elif c < M - k:
                    deletions += c
            min_deletions = min(min_deletions, deletions)

        return min_deletions