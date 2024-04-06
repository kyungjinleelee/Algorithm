"""
접근 방법
1. 기본적으로 '( )' 라는 짝이 되어야 올바른 괄호임
2. 스택에는 '(' 만 넣어두고 ')'이 들어올 때에만 삭제시킴
3. 스택에 비어있는데 ')'가 들어온다면 올바른 짝이 될 수 없으므로 False를 반환
4. for문을 다 돌았는데 stack 안에 '('가 남아있으면 올바른 짝이 아니므로 False를 반환
"""
def solution(s):
    answer = True
    stack = []
    # 문자열 s 크기만큼 반복
    for i in s:
        if i == "(":
            stack.append("(")
            
        # ")" 일 경우
        else:
            # 만약 빈 스택에 ")"이 들어올 때 
            if stack == []:
                return False
            
            # 스택 안에 "("가 있고 ")"가 들어와 올바른 괄호
            else:
                stack.pop()
                
    # for문이 다 끝났는데도 "(" 괄호가 남아있는 경우
    if stack != []:
        return False

    return True