def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):  # i 이후의 인덱스부터 순회
            answer.append(numbers[i] + numbers[j])
    answerset = set(answer)     # 중복 제거
    answer = list(answerset)    # 다시 리스트로 변환
    answer.sort()
    return answer
