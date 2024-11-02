def solution(keymap, targets):
    # 1. 각 문자별 최소 입력 횟수를 저장하는 딕셔너리 생성
    min_keypress = {}
    for key in keymap:
        for idx, char in enumerate(key):
            if char in min_keypress:
                min_keypress[char] = min(min_keypress[char], idx + 1)
            else:
                min_keypress[char] = idx + 1

    # 2. 각 target 문자열에 대해 최소 입력 횟수 계산
    result = []
    for target in targets:
        total_keypress = 0
        for char in target:
            if char in min_keypress:
                total_keypress += min_keypress[char]
            else:
                # 입력 불가능한 문자가 있으면 -1을 추가하고 종료
                total_keypress = -1
                break
        result.append(total_keypress)
    
    return result