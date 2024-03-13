def solution(answers):
    answer = []
    
    # 각 수포자의 찍기 패턴 리스트로 정의 
    case1 = [1,2,3,4,5]
    case2 = [2,1,2,3,2,4,2,5]
    case3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 세 명의 수포자 점수를 저장할 리스트 0으로 초기화
    scores = [0]*3
    
    for i in range(len(answers)):
        # 현재 문제의 정답과 수포자 1의 찍기 패턴을 비교하여 정답이 맞으면 해당 수포자의 점수를 1 증가
        if answers[i] == case1[i%5]:
            scores[0] += 1     
            
        if answers[i] == case2[i%8]:
            scores[1] += 1
            
        if answers[i] == case3[i%10]:
            scores[2] += 1
    
    # 수포자의 수만큼 반복
    for i in range(len(scores)):
        # 각 수포자의 점수가 최대 점수와 같으면 해당 수포자의 번호를 정답 리스트에 추가
        if scores[i] == max(scores):
            answer.append(i + 1)    # 수포자의 번호는 1부터 시작하므로 i + 1을 추가

    return answer