from itertools import permutations

def solution(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    unique_numbers = set()

    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            num = int(''.join(perm))
            unique_numbers.add(num)

    prime_count = sum(1 for num in unique_numbers if is_prime(num))
    
    return prime_count
    
    