class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(prefix: int) -> int:
            cur, nxt, total = prefix, prefix + 1, 0
            while cur <= n:
                total += min(n + 1, nxt) - cur
                cur *= 10
                nxt *= 10
            return total

        curr = 1
        k -= 1
        while k > 0:
            cnt = count(curr)
            if k >= cnt:
                k -= cnt
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr
