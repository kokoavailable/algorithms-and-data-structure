def solution(n, t, m, p):
    answer = ''
    str1 = ''
    turn_tube = []
    # 최소 turn_tube[-1] 갯수는 가지고 있어야 함.
    
    # 0 1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 1 4
    # 튜브의 순서를 일단 구해보자. 1 
    
    def convert(num, base):
        """ 숫자를 base 진법으로 변환한 문자열 반환 """
        chars = "0123456789ABCDEF"
        
        if num == 0:
            return "0"
        result = ""
        while num > 0:
            result = chars[num % base] + result
            num //= base
        return result 
    
    max_length = t * m
    sequence = ""
    num = 0
    while len(sequence) < max_length:
        sequence += convert(num, n)
        num += 1
            
    
    result = ""
    for i in range(t):
         result += sequence[m * i + p - 1]

    
    
    
    return result
