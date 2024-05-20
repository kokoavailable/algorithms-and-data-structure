from collections import Counter

def solution(X, Y):
    # 개수를 사용한 딕셔너리를 만들고 하나씩 카운트를 차감해야한다.
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    common_digits = []
    for digit in range(10):
        digit_str = str(digit)
        if digit_str in count_X and digit_str in count_Y:
            common_count = min(count_X[digit_str], count_Y[digit_str])
            common_digits.extend([digit_str] * common_count)
            
    if not common_digits:
        return "-1"
    
    common_digits.sort(reverse=True)
    result = ''.join(common_digits)
    
    if result[0] == '0':
        return '0'
    
    return result