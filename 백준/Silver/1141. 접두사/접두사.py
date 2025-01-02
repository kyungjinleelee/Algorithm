# 입력받기
n = int(input())
words = [str(input()) for _ in range(n)]

# 문자열의 길이가 짧은 순서대로 정렬
words.sort(key=len)

cnt = 0
for i in range(n):
    is_prefix = False # 접두어인지 아닌지 변수
    # 현재 단어보다 길이가 긴 단어를 확인
    for j in range(i + 1, n):
        # 현재 단어가 접두사인지 확인
        if words[i] == words[j][0:len(words[i])]:
            is_prefix = True
            break

    # 접두어 관계가 없는 경우에만 현재 단어 word를 추가
    if not is_prefix:
        cnt += 1

print(cnt)