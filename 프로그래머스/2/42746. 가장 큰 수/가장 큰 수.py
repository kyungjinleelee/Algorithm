def solution(numbers):
    # 각 숫자를 문자열로 변환하고, 비교를 위해 각 문자열을 3번 반복한 값을 기준으로 내림차순 정렬
    sorted_numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    
    # 정렬된 문자열을 합쳐 가장 큰 수 생성
    answer = ''.join(sorted_numbers)
    
    # 모든 숫자가 "0"인 경우, "0"을 반환
    return '0' if answer[0] == '0' else answer