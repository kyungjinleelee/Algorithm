def solution(numlist, n):
    # key 매개변수에 정렬 기준을 설정
    # (n과의 거리, -숫자)로 정렬
    return sorted(numlist, key=lambda x: (abs(x - n), -x))