def solution(s):
    char_count = {}

    # 각 문자의 등장 횟수를 계산
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    # 한 번만 등장하는 문자들만 필터링
    unique_char = []
    for char in char_count:
        if char_count[char] == 1:
            unique_char.append(char)
            
    # 사전 순으로 정렬
    unique_char.sort()

    # 리스트를 문자열로 변환해서 반환
    return ''.join(unique_char)