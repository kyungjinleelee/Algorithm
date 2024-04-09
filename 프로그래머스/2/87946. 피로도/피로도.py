from itertools import permutations

def solution(k, dungeons):
    answer = -1
    array = list(permutations(dungeons, len(dungeons)))
    
    for each in array:
        pirodo = k  # 현재 피로도
        check = 0   # 탐험한 던전 수
        
        for dungeon in each:
            # 현재 피로도가 현재 던전의 피로도보다 크거나 같으면 피로도 차감, 탐험한 던전 수 증가
            if pirodo >= dungeon[0]:
                pirodo -= dungeon[1]
                check += 1
            # 그렇지 않으면 다음 던전으로 ..
            else:
                continue
                
        if answer < check:
            answer = check
    return answer