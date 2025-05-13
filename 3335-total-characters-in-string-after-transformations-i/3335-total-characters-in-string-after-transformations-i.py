class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # t번 트랜스 포메이션 해서 문자열의 갯수를 구한다.
        # 문자열의 갯수가 늘어나는 순간은 z를 초과했을때 늘어난다..
        # 하지만 늘어나고서도 다시 그 스트링에 대해서 평가를 계속해야함.
        # t % s를 순회하면서 t를 k 번 바꾼다면 ? .. 상태가 계속 바뀜.. 순차적으로 해줘야할 듯.. 근데 브루탈로 가기에는 .. 시간복잡도가 너무 힘듬 .. 수학적 모델링이 가능할까 ? 하나가 한번 바뀜 .. ab의 탄생. 하나는 25 번에 바뀌고 하나는 26번에 바뀌고 .. 
        MOD = 10**9 + 7
        dp = [0] * 26
        for ch in s:
            dp[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_dp = [0] * 26
            for i in range(26):
                if i == 25:
                    new_dp[0] = (new_dp[0] + dp[25]) % MOD # a
                    new_dp[1] = (new_dp[1] + dp[25]) % MOD # b
                else:
                    new_dp[i+1] = (new_dp[i+1] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD
