"""
문제에서 최소 1개의 의상을 입어야 한다고 했으므로, 
경우에 따라 어떤 종류는 착용하지 않을 수도 있다는 점을 생각하자
<경우의 수>
(N+1)(M+1) = NM + N + M + 1

NM: N과 M을 모두 사용하는 경우
N: N만 사용하는 경우
M: M만 사용하는 경우
1: 모두 사용하지 않는 경우 
"""
def solution(clothes):
    # 각 종류 별 가진 의상을 저장 (종류:[이름, 이름, ...])
    # 종류를 key로 하는 딕셔너리 만듦
    closet = {}
    
    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]
            
    # A의 종류가 N개, B의 종류가 M개일 때 가능한 모든 경우의 수 (N+1)(M+1)
    answer = 1
    for _, value in closet.items():
        answer *= (len(value) + 1)
        
    # 아무것도 입지 않은 경우 1을 제외 
    return answer -1
