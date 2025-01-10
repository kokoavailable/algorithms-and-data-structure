def solution(array, commands):
    
    answer = []
    answer = list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1],commands))
    return answer