"""
동적 프로그래밍의 기본 개념
1. 분할정복
merge sort
2. 중복되는 하위 문제
피보나치 수열 (메모이 제이션)
3. 최적 부분 구조
0-1 배낭 문제.
"""

# Top-Down(메모이 제이션, memoization)
"""
탑 다운 방식은 재귀를 사용하여 문제를 해결하며, 중간 결과를 저장해 동일한 하위 문제의 중복 계산을 막는다.
재귀 호출을 통해 큰 문제를 해결하느 ㄴ과정에서. ㄱ이미 계산된 하위 문제의 결과를 메모이 제이션 테이블(배열이나 딕셔너리)에 저장하고 재사용 한다
"""

def fib_memo(n, memo={}):
  if n in memo:
    return memo[n]
  if n <= 1:
    return n
  memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
  return memo[n]

# Bottom-Up 테이블 화
"""
하위 문제부터 해결해 나가며, 결과를 테이블에 저장한다.
작은 하위 문제부터 시작해 점진적으로 더 큰 문제를 해결한다. 이 과정에서 하위 문제 결과를 이용해 상위 문제를 해결한다.
"""

def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
