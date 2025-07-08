class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        
        for i in range(n-1):
            cur, cnt, nxt = s[0], 0, []
            for digit in s:
                if digit == cur:
                    cnt += 1
                else:
                    nxt.append(str(cnt))
                    nxt.append(cur)
                    cur, cnt = digit, 1

            nxt.append(str(cnt))
            nxt.append(cur)
            s = "".join(nxt)

        return s

