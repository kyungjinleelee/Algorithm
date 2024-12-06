def calculate_bracket_value(input_str):
    stack = []
    value = 0   # 전체 괄호열의 값
    temp = 1    # 중간 값을 계산하기 위한 변수

    for i in range(len(input_str)):
        char = input_str[i]

        if char == '(':
            stack.append(char)
            temp *= 2
        elif char == '[':
            stack.append(char)
            temp *= 3
        elif char == ')':
            # 스택이 비어있거나, 스택 마지막 값이 ( 가 아니면 유효하지 않은 경우임
            if not stack or stack[-1] != '(':
                return 0
            # 문자열이 첫 번째 경우가 아니며, 직전 문자가 ( 이면 "()"가 완성된 경우임
            if i > 0 and input_str[i - 1] == '(':
                value += temp
            stack.pop()
            temp //= 2
        elif char == ']':
            if not stack or stack[-1] != '[':
                return 0
            if i > 0 and input_str[i - 1] == '[':
                value += temp
            stack.pop()
            temp //= 3
        else:
            return 0
    return value if not stack else 0

# 입력 및 실행
input_str = input()
result = calculate_bracket_value(input_str)
print(result)