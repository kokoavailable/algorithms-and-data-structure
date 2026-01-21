class Solution:
    def totalNQueens(self, n: int) -> int:
        ALL = (1 << n) - 1  # n개 비트가 1인 마스크

        def dfs(cols: int, diag1: int, diag2: int) -> int:
            if cols == ALL:
                return 1

            count = 0
            available = ALL & ~(cols | diag1 | diag2)

            while available:
                pos = available & -available
                available -= pos

                count += dfs(
                    cols | pos,
                    ((diag1 | pos) << 1) & ALL,
                    ((diag2 | pos) >> 1) & ALL
                )
            return count

        half = n // 2
        total = 0

        for c in range(half):
            pos = 1 << c
            total += dfs(pos, (pos << 1) & ALL, (pos >> 1) & ALL)
        total *= 2

        if n % 2 == 1:
            pos = 1 << half
            total += dfs(pos, (pos << 1) & ALL, (pos >> 1) & ALL)

        return total


