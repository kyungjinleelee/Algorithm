from collections import Counter

def solution(array):
    frequency = Counter(array)
    
     # 빈도를 내림차순으로 정렬
    most_common = frequency.most_common() # [(3, 3), (1, 1), (2, 1), (4, 1)]
    
    # 최빈값이 여러 개일 경우
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    # 그게 아니면 (최빈값이 한개면)
    return most_common[0][0]