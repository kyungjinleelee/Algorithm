def solution():
    # 입력 처리
    N = int(input())  # 크레인의 개수
    cranes = list(map(int, input().split()))  # 각 크레인의 무게 제한
    M = int(input())  # 박스의 개수
    boxes = list(map(int, input().split()))  # 각 박스의 무게

    # 내림차순 정렬
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)

    # 만약 가장 큰 크레인이 가장 무거운 박스를 못 옮기면 -1 반환
    if boxes[0] > cranes[0]:
        print(-1)
        return

    # 박스를 deque로 변환하지 않고 리스트로 유지
    time = 0
    while boxes:
        time += 1
        for crane in cranes:
            # 각 크레인에 대해 박스 리스트에서 들 수 있는 가장 무거운 박스를 찾고 제거
            for i in range(len(boxes)):
                if crane >= boxes[i]:
                    boxes.pop(i)  # 박스를 처리
                    break  # 해당 크레인은 일을 했으므로 다음 크레인으로 넘어감
    
    print(time)

# 함수 호출 예시
solution()
