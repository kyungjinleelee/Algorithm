def solution(s):
    result = []
    
    # 문자열을 공백을 기준으로 단어로 나눔
    words = s.split(" ")
    
    for word in words:
        new_word = ""
        for i, char in enumerate(word):
            # 짝수번째 인덱스는 대문자로, 홀수번째 인덱스는 소문자로
            if i % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        result.append(new_word)
    
    # 단어를 다시 공백으로 연결하여 반환
    return " ".join(result)
