def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        doll = 0
        # 현재 크레인 작동에 뽑힐 인형 번호 구하기
        for i in range(len(board)):
            if board[i][move-1] != 0:
                doll = board[i][move-1] # 인형 있으면 (0 아니면) 해당 번호 doll에 저장
                board[i][move-1] = 0    # 인형 뽑았으면 자리 비워줌
                break
        # 뽑힌 인형 없으면 계속 작동 
        if doll == 0:
            continue
        
        # 바구니에 같은 인형 연속해서 쌓인 경우 터트려벌임
        if stack and stack[-1] == doll:
            answer += 2         # 갯수 카운트
            stack.pop()
        else:
            stack.append(doll)  # 연속하지 않으면 그냥 바구니에 추가
    return answer