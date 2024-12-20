n = int(input())
words = list(set([input().strip() for _ in range(n)]))

def sort():
    # 정렬: (길이, 단어) 기준
    words.sort(key=lambda word: (len(word), word))
    
    # 출력
    for word in words:
        print(word)
sort()