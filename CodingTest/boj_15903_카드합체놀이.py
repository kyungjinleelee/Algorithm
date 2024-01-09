"""
자연수가 쓰여진 카드를 n장 갖고 있다. 카드 합체를 총 m번 하면 놀이가 끝난다.
m번의 합체를 모두 끝낸 뒤, n장의 카드에 쓰여있는 수를 모두 더한 값이 이 놀이의 점수가 된다. 
만들 수 있는 가장 작은 점수를 계산하는 프로그램을 만들어보자.
"""
import sys

input = sys.stdin.readline    # 값 입력받기
n, m = map(int, input().split())
card = list(map(int, input().split()))

for _ in range(m):
    card.sort()    # 카드리스트를 오름차순으로 정렬
    # 정렬된 카드 리스트에서 가장 작은 두 값을 선택해서, 두 값을 더한 값으로 대체 
    card[0], card[1] = card[0] + card[1], card[0] + card[1]

print(sum(card))    # 반복문 종료 후 카드 리스트에 있는 모든 값 출력
