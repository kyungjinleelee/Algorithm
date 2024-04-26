def solution(a, b, c):
    # 모든 숫자가 다를 경우
    if a != b and b != c and a != c:
        return a + b + c
    # 두 숫자가 같고 나머지 하나가 다를 경우
    elif (a == b and b != c) or (a != b and b == c) or (a == c and b != a) :
        return (a + b + c) * (a**2 + b**2 + c**2)
    # 모든 숫자가 같을 경우
    else:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)