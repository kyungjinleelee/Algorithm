def bucket(s):
    stack = []
    for i in s:
        # 예외 처리
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else: 
                stack.append(i)
    return True if len(stack) == 0 else False
            

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if bucket(s): answer += 1
        s = s[1:] + s[:1]
    return answer