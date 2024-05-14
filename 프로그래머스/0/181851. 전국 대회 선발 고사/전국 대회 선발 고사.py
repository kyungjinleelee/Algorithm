def solution(rank, attendance):
    answer = 0
    available_students = []
    
    # 참석 가능한 학생들의 등수와 학생 번호를 리스트에 추가
    for i in range(len(rank)):
        if attendance[i]:
            available_students.append((rank[i], i))
    
    # 등수를 기준으로 정렬
    available_students.sort()
    
    # 선발된 학생들의 번호 계산
    a, b, c = available_students[:3]
    
    return 10000 * a[1] + 100 * b[1] + c[1]