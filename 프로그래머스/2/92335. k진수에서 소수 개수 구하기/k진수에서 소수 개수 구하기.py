def convert_to_base_k(n,k):
    result = ""
    while n > 0:
        result = str(n % k) + result
        n = n // k
    return result

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def solution(n, k):
    k_base_str = convert_to_base_k(n, k)
    parts = k_base_str.split('0')
    
    prime_count = 0
    for part in parts:
        if part and is_prime(int(part)):
            prime_count += 1
            
    return prime_count
    

    
    
    return answer





