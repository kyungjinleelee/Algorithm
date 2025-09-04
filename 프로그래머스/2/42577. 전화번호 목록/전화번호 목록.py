def solution(phone_book):
    # 접두어 검사 누락을 막기 위해 정렬
    # 또한 정렬 시 접두어 검사를 효율적으로 할 수 있음
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True