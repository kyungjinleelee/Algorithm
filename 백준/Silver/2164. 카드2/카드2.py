from collections import deque
N = int(input())

# 카드 큐 생성
card = deque(range(1, N + 1)) # deque([1, 2, 3, 4, 5, 6])

# 카드 섞기
def card_mix():
    while len(card) > 1:   # 카드가 한 장 남을 때까지 반복
        # 제일 위에 있는 카드 바닥에 버림
        card.popleft()
        # 그 다음 위에 있는 카드는 제일 아래에 있는 카드 밑으로 옮김
        card.append(card.popleft())
    print(card[0])

card_mix() # 함수 호출