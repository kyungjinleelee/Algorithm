def solution(my_string):
    counts = [0] * 52
    for char in my_string:
        # 대문자인 경우
        if 'A' <= char <= 'Z':
            counts[ord(char) - ord('A')] += 1
        # 소문자인 경우
        elif 'a' <= char <= 'z':
            counts[ord(char) - ord('a') + 26] += 1
    return counts