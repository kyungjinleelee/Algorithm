# 입력 처리
s = input()
n = int(input())
words = set([input().strip() for _ in range(n)]) # 빠른 검색을 위해 단어 목록을 집합으로 저장
# ['software', 'contest']
visited = [False] * (len(s) + 1)

# 조합으로 생성해서 만들어보기
def find(current, index):
    if visited[index]:
        return
    visited[index] = True
    if current == s:
        return
    for word in words:
        if len(current) + len(word) > len(s):
            continue
        if s[index: index + len(word)] == word:
            find(current + word, index + len(word))
    return

find('', 0)
print(1 if visited[-1] else 0)