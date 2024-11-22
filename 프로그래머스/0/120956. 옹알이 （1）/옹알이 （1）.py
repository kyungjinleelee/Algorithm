# 정규 표현식으로 문자열 패턴을 반복 탐색해서 문자열 재구성
# 그 후 원래 문자열과 비교
import re

def solution(babbling):
    # 발음 가능한 단어 패턴
    valid_pattern = re.compile(r'^(aya|ye|woo|ma)+$')
    cnt = 0
    
    for word in babbling:
        # 패턴이 완전 일치하는 경우에만 카운트 증가
        if valid_pattern.fullmatch(word):
            cnt += 1
            
    return cnt