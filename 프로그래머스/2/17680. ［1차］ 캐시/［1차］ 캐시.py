from collections import deque

def solution(cacheSize, cities):
    
    # 캐시 크기에 따른 실행시간 측정 프로그램
    cache = deque(maxlen=cacheSize)
    
    total_time=0
    
    for city in cities:
        city = city.lower()
        if city in cache:
            # 캐시 hit
            cache.remove(city)
            cache.append(city)
            total_time += 1
        else:
            # 캐시 miss
            if len(cache) >= cacheSize and cacheSize > 0:
                cache.append(city)
            elif cacheSize > 0:
                cache.append(city)
            total_time += 5

    return total_time