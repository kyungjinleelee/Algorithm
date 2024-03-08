from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    # set으로 중복 제거
    report_dic = defaultdict(set)
    email_dic = defaultdict(int)
    
    # 신고 내용을 처리하기 위한 반복문 실행
    for i in range(len(report)):
        # 신고한 사용자와 신고당한 사용자로 분리
        report_from, report_to = report[i].split()
        # 신고당한 사용자를 key로 하는 report_dic에 신고한 사용자를 추가
        report_dic[report_to].add(report_from)

    # report_dic을 순회하면서 신고당한 사용자와 해당 사용자를 신고한 사용자들을 가져옴
    for report_to, reporters in report_dic.items():
        if len(reporters) >= k:
            # 해당 사용자를 신고한 사용자들을 순회하면서:
            for reporter in reporters:
                # 해당 사용자의 신고 이메일 수를 1 증가
                email_dic[reporter] += 1
    
    # 모든 사용자에 대해
    for name in id_list:
        # 해당 사용자가 받은 신고 이메일 수를 결과 리스트에 추가
        answer.append(email_dic[name])
    
    return answer