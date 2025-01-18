word = input()

# 크로아티아 알파벳 리스트
croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# 크로아티아 알파벳을 '*'로 치환
for alphabet in croatian_alphabets:
    word = word.replace(alphabet, "*")

# 치환된 문자열의 길이 출력
print(len(word))