from itertools import permutations

def solution(n, weak, dist): 
    leng = len(weak) # 점검 해야 할 외벽의 길이
    
    # weak의 길이 만큼 순회하면서, weak의 원소에 n을 더해서 원형 모양의 외벽을 펼쳐주기
    for x in range(leng):
        weak.append(weak[x] + n)
        
    # 모두 투입시켜도 안 될 때 -1 출력을 위해, dist의 길이보다 1 많게 저장
    answer = len(dist) + 1
    
    # 출발 지점을 weak의 길이만큼 순회
    for start in range(leng):
        # 친구들이 투입 될 시점은 permutations을 통해 변경
        for friends in list(permutations(dist, len(dist))):
            count = 0
            # 포지션 값: 친구들의 1시간동안 이동거리를 permutations로 뽑아낸 배열의 count - 1 번째의 값을 뺴준 것
            position = weak[start] - friends[count - 1]
            
            # 취약점 시작부분(start) 부터 start + leng 까지 순회하면서,
            for index in range(start, start + leng):
                # 현재 포지션 값이 취약점 배열의 index 값보다 작으면 count 갱신
                if position < weak[index]:
                    count += 1
                    # count가 친구의 수 넘으면 바로 중단
                    if count > len(dist):
                        break
                    # 그게 아니면 작업 후 position 갱신
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
            
    if answer > len(dist):
        return -1
    
    return answer