def solution(s):
    answer = 0
    idx = 0
    
    while idx < len(s):
        x = s[idx]
        cnt_same = 0
        cnt_diff = 0
        
        for i in range(idx, len(s)):
            if s[i] == x:
                cnt_same += 1
            else:
                cnt_diff += 1
            
            if cnt_same == cnt_diff:
                answer += 1
                idx = i + 1
                break
        
        else:
            answer += 1
            break
    
    return answer
        