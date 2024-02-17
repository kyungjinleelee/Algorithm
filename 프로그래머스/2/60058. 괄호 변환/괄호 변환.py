# 문자열 u, v로 분리하는 함수 
def separate(p):
    open_p, close_p = 0, 0  # 초기화
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:] # u, v

# 문자열 u가 올바른 괄호 문자열인지 체크하는 함수 (구현못함)
def check_balance(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
# return not stack
# return True if not stack else False

def solution(p):
    # 과정 1
    if not p:
        return p    
    # 과정 2
    u, v = separate(p)
    
    # 과정 3
    if check_balance(u):
        return u + solution(v)  # 재귀, 문자열 v에 대해 1단계부터 다시 수행, u에 이어 붙인 후 반환
    # 과정 4 (올바른 괄호 문자열이 아니라면?)
    else:
        answer = '('            # 과정 4-1
        answer += solution(v)   # 과정 4-2
        answer += ')'           # 과정 4-3
        
        for pp in u[1:len(u) - 1]:  # 과정 4-4
            #괄호 방향을 뒤집어서 붙이기
            if pp == '(':
                answer += ')'
            else:
                answer += '('
        return answer