from collections import defaultdict

def solution(clothes):
    # 카테고리별 의상의 수 딕셔너리
    clothes_dict = defaultdict(int)
    
    for item, category in clothes:
        clothes_dict[category] += 1
    
    # 모든 종류의 의상에 대해 선택할 수 있는 경우의 수.
    combinations = 1
    for count in clothes_dict.values():
        combinations *= (count + 1) # 선택하지 않는 경우의 수를 포함한다..
    
    # 최소 한개의 의상은 입어야 한다.
    return combinations - 1 