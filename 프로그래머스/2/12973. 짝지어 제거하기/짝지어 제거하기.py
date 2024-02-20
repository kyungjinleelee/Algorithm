def solution(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        # 짝 맞으면 pop
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print('이경진 짱')
    
    # 다 pop 해서 0 되면 1 반환
    if len(stack) == 0:
        return 1
    else:
        return 0

    