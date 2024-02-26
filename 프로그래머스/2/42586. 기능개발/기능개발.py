def solution(progresses, speeds):
    answer = []
    
    # 작업 리스트가 빌 때까지 반복
    while progresses:
        cnt = 0
        # 작업 리스트가 남아있고 && 맨 앞의 작업 진도율이 100이면 cnt 증가 > 작업 리스트와 작업 속도 리스트에서 제거
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        
        # 리스트가 비면 작업 리스트의 진도를 증가
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        
        # 배포됐다고 결과리스트에 추가
        if cnt:
            answer.append(cnt)
    return answer