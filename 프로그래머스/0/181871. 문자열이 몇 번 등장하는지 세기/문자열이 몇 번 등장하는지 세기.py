def solution(myString, pat):
    answer = 0
    # 문자열에서 패턴의 길이만큼씩 잘라내어 패턴과 일치하는지 확인
    for i in range(len(myString) - len(pat) + 1):
        # 현재 위치에서 패턴과 일치하는 경우
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer