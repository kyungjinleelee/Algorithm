def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if not answer: # 예외 처리 -> 루프가 끝난 후, 리스트 비어 있는지 체크
        return [-1]
    
    return sorted(answer)