def solution(s):
    answer = []
    
    s = s[2:-2]
    s = s.split("},{")
    
    s = [set(map(int, group.split(","))) for group in s]
    
    
    s.sort(key=len)
    
    result = []
    
    for group in s:
        for num in group:
            if num not in result:
                result.append(num)
    
    return result