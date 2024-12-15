def solution(cards1, cards2, goal):
    for g in goal:
        # cards1이 비어있지 않으면서 첫 번째 카드와 일치하는 경우
        if cards1 and g == cards1[0]:
            cards1.pop(0)   # 첫 번째 카드를 제거
        # cards2이 비어있지 않으면서 첫 번째 카드와 일치하는 경우
        elif cards2 and g == cards2[0]:
            cards2.pop(0)   # 첫 번째 카드를 제거
        else:
            return "No"     
    return "Yes"