def solution(arr, queries):
    answer = []
    for i in range(len(arr)):
        for j in range(len(queries)):
            if queries[j][0] <= i and i <= queries[j][1]:
                arr[i] += 1
    return arr