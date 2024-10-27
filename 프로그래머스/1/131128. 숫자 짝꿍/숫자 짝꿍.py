from collections import Counter

def solution(X, Y):
    # 각 숫자의 빈도 계산
    x_count = Counter(X)  # 출력 예시: 	Counter({'0': 2, '1': 1})
    y_count = Counter(Y)
    
     # 공통 숫자 중에서 최대로 짝지을 수 있는 숫자 모으기
    pairs = []
    for digit in x_count:
        if digit in y_count:
            # 각 숫자별로 공통 개수만큼 짝지음
            common_count = min(x_count[digit], y_count[digit])
            pairs.extend([digit] * common_count)
            
    # 짝지어진 숫자들을 내림차순 정렬
    pairs.sort(reverse=True)
    
    # 결과 생성
    result = ''.join(pairs)
    
    # 예외 처리
    if not result:           # 공통 숫자가 없으면
        return "-1"
    if result[0] == "0":     # 짝지은 숫자가 모두 0인 경우
        return "0"
    
    return result