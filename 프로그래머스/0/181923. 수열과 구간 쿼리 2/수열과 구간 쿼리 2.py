def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        min_val = float('inf')
        
        for i in range(s, e + 1):
            # k보다 크고 현재까지의 최소값보다 작을 경우
            if arr[i] > k and arr[i] < min_val:
                # 최소값 갱신
                min_val = arr[i]
        # 최소값이 갱신되었다면 리스트에 추가
        if min_val != float('inf'):
            answer.append(min_val)
        # 최소값이 초기값이면 -1을 추가
        else:
            answer.append(-1)
        
    return answer