def solution(emergency):
    sorted_emergency = sorted(emergency, reverse = True)
    answer = []
    
    for e in emergency:
        rank = sorted_emergency.index(e) + 1
        answer.append(rank)
        
    return answer