def solution(polynomial):
    x_sum = 0  # x가 포함된 항의 계수 합
    constant_sum = 0  # 상수항의 합
    
    for term in polynomial.split(' + '):
        # 일차항인 경우
        if 'x' in term:
            # 'x' 앞에 숫자가 있으면 계수로 처리하고, 없으면 계수를 1로 처리
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term[:-1])  # 'x' 제외한 부분을 정수로 변환하여 계수로 추가
        # 상수항인 경우
        else:
            constant_sum += int(term)
    
    result = []
    # 일차항을 결과에 추가
    if x_sum > 0:
        if x_sum == 1:
            result.append('x')
        else:
            result.append(f'{x_sum}x')
    # 상수항을 결과에 추가
    if constant_sum > 0:
        result.append(str(constant_sum))
    
    # 결과를 ' + '로 연결하여 반환
    return ' + '.join(result)