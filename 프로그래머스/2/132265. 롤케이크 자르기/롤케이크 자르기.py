from collections import Counter

def solution(topping):
    answer = 0
    # 우선 왼쪽이 모든 토핑을 갖고 있음
    left = Counter(topping)
    # 오른쪽은 아직 토핑이 없음
    right = {}
    
    # 순회하면서 오른쪽한테 하나씩 토핑을 나눠줌
    for i in range(len(topping)):
        # 토핑이 오른쪽에 이미 있으면, 해당 토핑의 수 1 증가
        if topping[i] in right:
            right[topping[i]] += 1
        else:
            right[topping[i]] = 1
            
        left[topping[i]] -= 1
        
        if not left[topping[i]]:
            del(left[topping[i]])
        
        # 왼쪽이 가진 토핑 갯수 == 오른쪽이 가진 토핑 갯수가 같으면 1 더함
        if len(left) == len(right):
            answer += 1
    return answer