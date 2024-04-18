def solution(s):
    # 문자열을 파싱하여 튜플을 집합으로 변환하는 함수
    def to_set(s):
        return set(map(int, s.split(',')))

    # 입력 문자열을 파싱하여 각 튜플을 집합으로 만듦
    parsed_data = s[2:-2].split("},{")
    dict_data = [to_set(elem) for elem in parsed_data]

    # 길이 순으로 정렬
    dict_data.sort(key=len)

    # 차집합을 이용하여 튜플의 순서대로 원소를 추출하여 answer에 저장
    answer = list(dict_data[0])
    for i in range(1, len(dict_data)):
        elem = dict_data[i] - dict_data[i - 1]
        answer.append(elem.pop())

    return answer

# 예시 입력
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))  # 출력: [2, 1, 3, 4]
