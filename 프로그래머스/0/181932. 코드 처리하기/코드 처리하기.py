def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        # '1'이면 모드 바꾸기
        if code[i] == '1':
            if mode == 0:
                mode = 1
            elif mode == 1:
                mode = 0
                
        if mode == 0:
            if code[i] != '1' and i % 2 == 0:
                ret += code[i]
        elif mode == 1:
            if code[i] != '1' and i % 2 != 0:
                ret += code[i]
    if ret:
        return ret
    else:
        return "EMPTY"