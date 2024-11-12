def solution(A, B):
    # A를 오른쪽으로 한 칸씩 밀어보며 비교
    for i in range(len(A)):
        if A == B:
            return i  # i번 밀었을 때 A와 B가 같다면 그 횟수 반환
        A = A[-1] + A[:-1]  # A를 한 칸 오른쪽으로 밀기
    
    return -1  # 모든 회전 후에도 B와 일치하지 않으면 -1 리턴