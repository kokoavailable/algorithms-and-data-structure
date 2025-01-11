from collections import deque
import math

def solution(progresses, speeds):
    result = []  # 배포 횟수 저장 리스트
    days = deque([math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))])
    
    current_max_day = days[0]
    count = 1

    for i in range(1, len(days)):
        if days[i] <= current_max_day:
            count += 1
        else:
            result.append(count)
            count = 1
            current_max_day = days[i]
    
    result.append(count)

    return result