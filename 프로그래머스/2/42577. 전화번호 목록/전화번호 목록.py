def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
        
    return True

#모든 숫자에 대해 검사해봐야 되나? 탐색에 있어서 해시는 매우 유리.