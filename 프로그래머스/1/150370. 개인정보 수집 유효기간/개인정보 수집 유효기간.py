from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜 변환
    today_date = datetime.strptime(today, "%Y.%m.%d")
    
    # terms를 딕셔너리로 만들기
    dic_terms = {}
    for i in range(len(terms)):
        split_terms = terms[i].split()
        term, date = split_terms[0], split_terms[1]
        dic_terms[term] = int(date)
        
    # 개인정보 유효기간 계산
    for idx, privacy in enumerate(privacies):
        collected_date, term_type = privacy.split()
        collected_date = datetime.strptime(collected_date, "%Y.%m.%d")
        print(collected_date) # 2019-01-01 00:00:00
        
        # 유효기간 추가
        expiration_date = collected_date + relativedelta(months=dic_terms[term_type])
        
        # 만료 날짜가 오늘 이전이면 파기 대상
        if expiration_date <= today_date:
            answer.append(idx + 1)
        
    # 오름차순으로 정렬 후 반환
    return sorted(answer)