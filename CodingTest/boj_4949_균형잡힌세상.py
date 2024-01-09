"""
입력된 문장에 소괄호("()")와 대괄호 ("[]")가 균형이 잘 맞는지
yes or no 로 출력하는 문제이다.
"""
while True :    # 입력을 계속 할 수 있도록 무한 루프 시작
    a = input()
    stack = []
    
    if a == ".":    # 문자열이 . 이면 반복문 종료
        break
        
    for i in a:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()    # 짝이맞으면 지워서 stack을 비워준다 (0으로 맞춰줌)
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        if len(stack) == 0:    # stack이 비워져있으면 yes 출력
            print('yes')
        else:                  # 그렇지 않으면 no 출력
            print('no')
