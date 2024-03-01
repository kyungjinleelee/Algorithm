def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    # 완주자의 길이만큼 반복 > participant 찾아서 없는 사람 찾기
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]
        
    # 예외 처리: 전부 다 돌아도 없을 땐 마지막 주자가 완주하지 못한 선수
    return participant[len(participant)-1]
    
