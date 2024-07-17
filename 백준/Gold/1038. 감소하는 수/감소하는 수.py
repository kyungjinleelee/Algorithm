def find_decreasing_number(N):
    from itertools import combinations
    
    # 모든 감소하는 수를 저장할 리스트
    decreasing_numbers = []
    
    # 숫자 0~9 중에서 조합을 이용해 감소하는 수 생성
    for length in range(1, 11):  # 자릿수 1개부터 10개까지
        for comb in combinations(range(10), length):
            number = int(''.join(map(str, sorted(comb, reverse=True))))
            decreasing_numbers.append(number)
            
    # 감소하는 수들을 오름차순으로 정렬
    decreasing_numbers.sort()
    
    # N번째 감소하는 수 반환 (없으면 -1)
    if N < len(decreasing_numbers):
        return decreasing_numbers[N]
    else:
        return -1

# 입력
N = int(input().strip())

# 결과 출력
print(find_decreasing_number(N))