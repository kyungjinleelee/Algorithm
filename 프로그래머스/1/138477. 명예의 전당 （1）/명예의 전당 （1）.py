def solution(k, score):
    answer = []
    honor = [] # 명예의 전당
    for i in range(len(score)):
        honor.append(score[i]) # score의 첫번째 요소를 집어넣음
        if len(honor) > k:
            honor.remove(min(honor))
        answer.append(min(honor)) # honor의 제일 작은 값(최하위 점수)를 answer에 넣음
    return answer