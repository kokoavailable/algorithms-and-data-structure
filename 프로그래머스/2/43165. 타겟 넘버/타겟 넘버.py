def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        else:
            return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
        
    return dfs(0, 0)

#           dfs(0, 0)
#          /         \
#     dfs(1, 1)     dfs(1, -1)
#     /     \       /      \
# dfs(2, 2) dfs(2, 0) dfs(2, 0) dfs(2, -2)