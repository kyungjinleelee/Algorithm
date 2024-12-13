def solution(name, yearning, photo):
    answer = []
    # 이름과 점수를 매핑하는 딕셔너리
    score = dict(zip(name, yearning))
    
    # 1. photo의 각 리스트와 그 원소들을 순회
    for i in range(len(photo)):
        # 2. 총 그리움 점수를 초기화하는 변수
        total = 0
        for j in range(len(photo[i])):
            # 3. 만약 해당 이름이 그리워하는 사람이라면 그리움 점수 추가
            if photo[i][j] in name:
                total += score[photo[i][j]]
        # 4. 정답 배열에 총 그리움 점수를 추가
        answer.append(total)
    return answer