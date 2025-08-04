def solution(name, yearning, photo):
    result = []
    # 이름 별 그리움 점수 매핑
    score = {n: y for n, y in zip(name, yearning)} # {'may': 5, 'kein': 10, 'kain': 1, 'radi': 3}
    
    for p in photo:
        total = 0
        for i in p:
            if i in score:
                total += score[i]
        result.append(total)
    return result