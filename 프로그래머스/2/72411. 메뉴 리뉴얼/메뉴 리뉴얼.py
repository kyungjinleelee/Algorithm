from itertools import combinations
from collections import Counter

def solution(orders, course):
    # orders: 주문 리스트
    # course: 가능한 코스 개수
    
    answer = [] 
    for k in course:    # 가능한 코스 갯수를 하나씩 반복
        candidates = []
        for menu_li in orders:  # orders에 있는 각 주문에 대해 반복
            # 현재 주문에서 가능한 길이가 k인 모든 조합을 만듦
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))   # 조합을 정렬하여 문자열로 변환
                candidates.append(res)      # 가능한 조합을 candidates 리스트에 추가
        # candidates 리스트에 있는 조합의 빈도수를 세고, 가장 빈번하게 나타나는 조합을 먼저 정렬
        sorted_candidates = Counter(candidates).most_common()
        # 가장 빈번하게 나타나는 조합 중에서 빈도수가 2 이상이고, 가장 빈도수가 높은 조합과 동일한 빈도수를 가지는 조합을 answer 리스트에 추가
        for menu, cnt in sorted_candidates:
            if cnt > 1 and cnt == sorted_candidates[0][1]:
                answer.append(menu)
        # answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]] 리스트 컴프리헨션으로 이렇게 한 줄로 줄일 수 있다!
    return sorted(answer)   # 최종 결과 오름차순으로 정렬해서 반환 
