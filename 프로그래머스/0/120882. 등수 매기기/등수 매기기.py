def solution(score):
    avg = []
    # 평균 점수를 구해 리스트에 넣기
    for char in score:
        avg.append(sum(char) / 2)
    # 내림차순으로 정렬
    sorted_avg = sorted(avg, reverse = True)
    
    # 각 학생의 평균 점수에 대한 순위를 구함
    ranks = [sorted_avg.index(a) + 1 for a in avg]
    
    return ranks