def solution(order):
    answer = 0
    for char in order:
        if 'americano' in char:
            answer += 4500
        elif 'cafelatte' in char:
            answer += 5000
        elif 'anything' in char:
            answer += 4500
    return answer