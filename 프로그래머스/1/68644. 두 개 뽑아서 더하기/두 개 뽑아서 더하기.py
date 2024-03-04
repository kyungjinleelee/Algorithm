def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answerset = set(answer) # 중복 제거
    answer = list(answerset)
    answer.sort()
    return answer