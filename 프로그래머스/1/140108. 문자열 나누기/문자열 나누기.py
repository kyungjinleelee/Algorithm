def solution(s):
    count = 0  # 분리된 문자열의 개수
    i = 0      # 문자열을 순회할 인덱스

    while i < len(s):
        x = s[i]            # 현재 부분의 첫 글자
        x_count = 0         # x 글자의 개수
        other_count = 0     # x 이외의 글자의 개수
        j = i               # 현재 위치

        # x와 x가 아닌 글자의 개수를 비교하면서 문자열 분리
        while j < len(s):
            if s[j] == x:
                x_count += 1
            else:
                other_count += 1
            
            # x와 x가 아닌 글자의 개수가 같으면 문자열 분리
            if x_count == other_count:
                count += 1  # 분리된 문자열 개수 증가
                break
            
            j += 1

        # 문자열이 끝났는데도 개수가 같아지지 않으면 마지막으로 분리
        if j == len(s):
            count += 1  # 마지막 부분 포함
            
        # 인덱스 위치를 분리된 다음 위치로 이동
        i = j + 1

    return count