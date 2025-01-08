from collections import Counter

s = input()
big_s = s.upper()

def most_frequency_char(big_s):
    # 알파벳 빈도 세기 (Counter는 문자열의 빈도를 O(n)의 시간 복잡도로 수행)
    counter = Counter(big_s)
    # print(counter) # Counter({'I': 4, 'S': 4, 'M': 1, 'P': 1})

    max_count = max(counter.values())
    most_common = []
    for char, count in counter.items():
        if count == max_count:
            most_common.append(char)

    if len(most_common) >= 2:
        return '?'
    else:
        return most_common[0]

print(most_frequency_char(big_s))