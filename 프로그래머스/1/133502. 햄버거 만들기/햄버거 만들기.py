def solution(ingredient):
    burger_count = 0
    stack = []

    for item in ingredient:
        # 스택에 재료 추가
        stack.append(item)
        
        # 스택의 끝에서 4개가 햄버거 패턴과 일치하면 포장
        if stack[-4:] == [1, 2, 3, 1]:
            # 햄버거 패턴 제거
            del stack[-4:]
            # 햄버거 개수 증가
            burger_count += 1
    
    return burger_count