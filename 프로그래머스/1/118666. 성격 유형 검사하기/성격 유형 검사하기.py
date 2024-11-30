def solution(survey, choices):
    # 각 성격 유형 점수를 저장할 딕셔너리
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 각 질문에 대해서 선택한 choices를 기반으로 점수 계산함
    for i in range(len(survey)):
        # survey[i]의 첫 번째 문자: 비동의 관련 유형
        # survey[i]의 두 번째 문자: 동의 관련 유형
        disagree, agree = survey[i][0], survey[i][1]
        choice = choices[i]
        
        # 비동의 선택 (선택지가 1, 2, 3)
        if choice < 4:
            scores[disagree] += 4 - choice
                
        # 동의 선택 (선택지가 5, 6, 7)
        elif choice > 4:
            scores[agree] += choice - 4
    
    # 점수가 같으면 사전 순으로 빠른 유형 선택 (정렬)
    answer = ''
    answer += 'R' if scores['R'] >= scores['T'] else 'T'
    answer += 'C' if scores['C'] >= scores['F'] else 'F'
    answer += 'J' if scores['J'] >= scores['M'] else 'M'
    answer += 'A' if scores['A'] >= scores['N'] else 'N'
    
    return answer