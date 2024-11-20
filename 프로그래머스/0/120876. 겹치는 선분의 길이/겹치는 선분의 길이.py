def solution(lines):
    # 좌표 범위는 -100부터 100까지 (총 201칸)
    coords = [0] * 201  # 모든 좌표 초기화

    # 선분의 시작점과 끝점을 카운팅
    for start, end in lines:
        for i in range(start, end):  # 선분의 범위만큼 1씩 증가
            coords[i + 100] += 1  # 좌표를 0 기반으로 이동하기 위해 +100

    # 두 개 이상의 선분이 겹친 부분의 길이 계산
    overlap_length = sum(1 for x in coords if x > 1)

    return overlap_length