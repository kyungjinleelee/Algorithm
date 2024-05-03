def solution(arr, queries):
    for query in queries:
        i, j = query
        # arr[i]와 arr[j] 값 서로 바꾸기
        arr[i], arr[j] = arr[j], arr[i]
    return arr