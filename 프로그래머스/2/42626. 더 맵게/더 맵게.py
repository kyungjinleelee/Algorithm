"""
가장 작은 값 부터 정렬된다? = MinHeap
파이썬이 제공하는 heapq 라이브러리는 기본적으로 MinHeap 구조이므로 라이브러리를 이용해 구현하면 됨 
"""
import heapq

def solution(scoville, K):
    answer = 0
    # 스코빌 지수 리스트를 heap 구조로 변환
    heapq.heapify(scoville)
    
    # 스코빌 리스트가 빌 때까지 반복 
    while scoville:
        # 리스트에서 가장 작은 값 꺼내기 
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        # 리스트에서 다음으로 작은 값 꺼내기
        second = heapq.heappop(scoville)
        # 새로운 스코빌 지수 score 계산
        score = first + (second * 2)
        heapq.heappush(scoville, score) # 계산된 score 다시 heapq에 추가
        answer += 1 # 섞은 횟수 1 증가
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer