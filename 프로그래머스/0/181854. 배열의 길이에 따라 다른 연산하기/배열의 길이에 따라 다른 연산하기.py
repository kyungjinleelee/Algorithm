def solution(arr, n):
    answer = []
    for i in range(len(arr)):
        if len(arr) % 2 != 0 and i % 2 == 0:
            answer.append(arr[i] + n)
        elif len(arr) % 2 == 0 and i % 2 != 0:
            answer.append(arr[i] + n)
        # 배열의 길이가 홀수이고 인덱스가 홀수이거나, 배열의 길이가 짝수이고 인덱스가 짝수인 경우
        else:
            answer.append(arr[i])
    return answer