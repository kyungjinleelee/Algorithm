from itertools import combinations

def solution(dots):
    # 가능한 모든 직선 조합
    pairs = [
        (0, 1, 2, 3),
        (0, 2, 1, 3),
        (0, 3, 1, 2)
    ]

    # 기울기를 비교
    for i, j, k, l in pairs:
        x1, y1 = dots[i]
        x2, y2 = dots[j]
        x3, y3 = dots[k]
        x4, y4 = dots[l]

        # 평행 조건 확인
        if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
            return 1  # 평행한 경우

    return 0  # 평행한 경우 없음