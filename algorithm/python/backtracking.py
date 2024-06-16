# 백트래킹 알고르짐
# 완전 탐색의 변형으로, 해답의 후보를 점진적으로 만들어가며 가능한 모든 경우의 수틀 탐색한다.
# 그러나 브루트 포스와 달리 백트래킹은 해답이 될 수 없는 경우의 수를 조기에 제거해 탐색 공간을 줄인다.
# 즉 부분 해답이 전체 해답이 될 가능성이 없을때, 그 부분 해답을 버린다. 


# 백트래킹의 일반적 인 구조
# 백트래킹 알고리즘은 다음과 같은 일반적 구조를 지닌다.
# 현재 단계에서 가능한 모든 후보 생성 -> 후보 해답이 문제의 제약 조건을 만족하는 지 검사 -> 후보 해답이 문제의 해답이 될 수 있는지 검사 -> 재귀 호출 -> 백트래킹(반복)

def backtrack_combinations(nums, path, start, result):
    result.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack_combinations(nums, path, i + 1, result)
        path.pop()

def find_combinations(nums):
    result = []
    backtrack_combinations(nums, [], 0, result)
    return result
