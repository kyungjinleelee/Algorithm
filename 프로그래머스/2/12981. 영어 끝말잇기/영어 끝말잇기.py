def solution(n, words):
    # checked 리스트에는 첫 번째 단어 넣어줌 (이미 나온 단어를 저장)
    checked = [words[0]]
    
    # 두 번째 단어부터 마지막 단어까지 반복 
    for i in range(1, len(words)):
        # 첫 번째 단어의 첫 글자와 1 -1 단어의 마지막 글자랑 비교 && 이전에 말한 적 없는지 
        if words[i][0] == words[i-1][-1] and words[i] not in checked:
            checked.append(words[i])
        else:
            return [(i%n)+1, (i//n)+1]
        
    return [0, 0]
