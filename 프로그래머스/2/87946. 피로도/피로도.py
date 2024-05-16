from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    for perm in permutations(dungeons):
        current_stamina = k
        count = 0
        
        for minimum_stamina, stamina_cost in perm:
            if current_stamina >= minimum_stamina:
                current_stamina -= stamina_cost
                count += 1
            else:
                break
                
        max_count = max(max_count, count)

        
    return max_count