def solution(k, m, score):
    answer = 0
    # 내림차순으로 정렬해서 높은 점수부터 상자 채우기
    score = sorted(score, reverse = True)
    # m개 씩 묶어서 상자 만들기
    for i in range(0, len(score) - m + 1, m):
        # 각 상자의 최소 점수는 score[i + m - 1]
        answer += score[i + m - 1] * m
    return answer