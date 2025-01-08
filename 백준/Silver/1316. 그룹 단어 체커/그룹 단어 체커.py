n = int(input())
words = [input() for _ in range(n)]

def is_group_word(word):
    seen = set()   # 이미 등장한 문자들을 저장할 집합
    last_char = '' # 이전 문자 저장

    for char in word:
        if char != last_char:
            if char in seen:
                return False
            seen.add(char)
        last_char = char
    return True

# 그룹 단어 갯수 새기
group_word_count = sum(1 for word in words if is_group_word(word))

print(group_word_count)