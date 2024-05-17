def solution(n, m, section):
    count = 0
    current_position = 0
    
    for sec in section:
        if sec > current_position:
            count += 1
            current_position = sec + m - 1
            
    return count