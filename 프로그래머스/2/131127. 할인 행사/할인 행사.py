def solution(want, number, discount):
    dic = {}
    answer = 0
    
    for i in range(len(want)):
        #사야할 품목과 그 갯수를 각각 key와 value로 딕셔너리 형성
        dic[want[i]] = number[i]
    i = 0    
    #discount의 원소를 10개씩 묶어 열흘동안 할인하는 목록 형성
    while i <= len(discount) - 10 : 
        shop = discount[i: i+10]
        con = True
        
        #열흘 중 사야할 품목이 할인하는 날의 수와 구매해야 할 수가 다르면 실행 종료
        for j in want:
            if shop.count(j) == dic[j]:
                continue
            else:
                con = False
                break
                
        #열흘 중 사야할 품목이 할인하는 날의 수와 구매해야 할 수가 모두 같으므로 answer 1 증가
        if con:
            answer += 1
        i += 1
    return answer

# 경계값테스트 