def solution(arr1, arr2):
    answer = []
    # 행 순회
    for i in range(len(arr1)):
        row = []
        # 열 순회
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        # 결과 행렬에 추가
        answer.append(row)
    return answer