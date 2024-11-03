def solution(s, skip, index):
    # 사용할 알파벳 필터링 (skip에 포함되지 않은 알파벳 리스트)
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    alphabet_len = len(alphabet)
    
    # 변환된 문자들을 담을 리스트
    result = []

    # s의 각 문자에 대해 변환
    for char in s:
        # 현재 문자의 위치를 alphabet 리스트에서 찾기
        current_index = alphabet.index(char)
        # index 만큼 이동한 위치 계산 (모듈로 연산으로 순환 이동)
        new_index = (current_index + index) % alphabet_len
        # 변환된 문자 추가
        result.append(alphabet[new_index])
    
    # 결과 리스트를 문자열로 합쳐서 반환
    return ''.join(result)