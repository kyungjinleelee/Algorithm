def solution(n, lost, reserve):
    # 도난당한 학생 중 여벌 체육복을 가진 학생은 빌려줄 수 없도록 중복 제거
    lost_only = set(lost) - set(reserve)
    reserve_only = set(reserve) - set(lost)

    # 여벌 체육복 빌려주기
    for student in sorted(reserve_only):
        # 앞번호 학생에게 빌려줄 수 있는지 확인
        if student - 1 in lost_only:
            lost_only.remove(student - 1)
        # 뒷번호 학생에게 빌려줄 수 있는지 확인
        elif student + 1 in lost_only:
            lost_only.remove(student + 1)

    # 체육복을 가진 학생 수: 전체 학생 수 - 아직도 체육복이 없는 학생 수
    return n - len(lost_only)