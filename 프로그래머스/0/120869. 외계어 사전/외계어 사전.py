def solution(spell, dic):
    # spell을 정렬한 문자열 생성
    sorted_spell = ''.join(sorted(spell))
    
    # dic의 각 단어를 정렬하고 spell과 일치하는지 확인
    for word in dic:
        if ''.join(sorted(word)) == sorted_spell:
            return 1
    return 2