def solution(babbling):
    # 발음 가능한 단어 목록
    words = ["aya", "ye", "woo", "ma"]
    count = 0
    
    # 각 단어를 순회
    for b in babbling:
        # 발음할 수 있는 패턴인지 확인하기 위해 임시 변수에 단어 저장
        temp = b
        # 연속된 발음을 확인하기 위한 마지막 발음
        last_word = ""
        
        for word in words:
            # 발음 패턴을 찾아서 공백으로 변경
            temp = temp.replace(word, " ")
        
        # 공백으로 변환된 temp가 모두 빈 문자열이면 발음 가능
        if temp.strip() == "":
            # 연속된 발음을 확인하기 위해 비교
            for word in words:
                if word * 2 in b:  # 동일한 발음이 연속된 경우
                    break
            else:
                count += 1
    return count