def solution(s):
    answer = 0
    idx = 0
    
    # 그 서브스트링의 첫 인덱스를 추적해야 한다.
    
    while idx < len(s):
        x = s[idx]
        cnt_same = 0
        cnt_diff = 0
        
        for char in s[idx:]:
            idx += 1

            if char == x:
                cnt_same += 1
            else:
                cnt_diff += 1

            if cnt_same == cnt_diff:
                answer += 1
                break
        
        else:
            answer += 1
            break
            
    return answer
        
    return answer