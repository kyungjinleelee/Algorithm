def solution(quiz):
    answer = []
    # quiz 리스트에서 공백을 기준으로 나눠서 X, 연산자, Y, Z에 할당
    # 연산자의 경우의 수를 +와 -로 나눠서 계산 수행
    # 수식 계산해서 참이면 "O", 틀리면 "X" 를 정답 리스트에 넣고 반환
    for q in quiz:
        parts = q.split()
        
        X = int(parts[0])
        operator = parts[1]
        Y = int(parts[2])
        Z = int(parts[-1])
        
        if operator == '+':
            if X + Y == Z:
                answer.append("O")
            else:
                answer.append("X")
        elif operator == '-':
            if X - Y == Z:
                answer.append("O")
            else:
                answer.append("X")
                
    return answer