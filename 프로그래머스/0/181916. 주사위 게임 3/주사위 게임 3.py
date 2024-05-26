def solution(a, b, c, d):
    # 주사위 숫자를 리스트에 담고 정렬
    dice = [a, b, c, d]
    dice.sort()
    
    # 주사위 숫자의 빈도를 카운트
    count = {}
    for num in dice:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    # 숫자가 모두 같을 때
    if len(count) == 1:
        p = dice[0]
        return 1111 * p
    # 세 주사위가 같거나 or 두 개씩 같은 값일 경우
    elif len(count) == 2:  # ex) [4, 4, 4, 1] or [6, 3, 3, 6]
        values = list(count.values())
        keys = list(count.keys())
        # 세 주사위가 같은 경우
        if 3 in values:
            p = keys[values.index(3)] # 3번 나온 숫자
            q = keys[values.index(1)] # 1번 나온 숫자
            return (10 * p + q) ** 2
        # 두 개씩 같은 숫자가 나오는 경우
        else:
            p, q = keys
            return (p + q) * abs(p - q)
    # 두 주사위가 같은 숫자가 나오는 경우 ex) [4, 4, 1, 3]
    elif len(count) == 3:
        values = list(count.values())
        keys = list(count.keys())
        p = keys[values.index(2)] # 2번 나온 숫자
        keys.remove(p)
        q, r = keys
        return q * r
    # 네 주사위의 숫자가 모두 다를 경우
    else:
        return min(dice)