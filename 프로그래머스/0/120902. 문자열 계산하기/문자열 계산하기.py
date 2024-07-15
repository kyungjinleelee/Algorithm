def solution(my_string):
    answer = 0
    # 문자열을 공백을 기준으로 분리
    tokens = my_string.split()
    
    # 첫 번째 숫자를 결과값으로 초기화
    answer = int(tokens[0])
    
    # 연산자를 기준으로 숫자를 처리
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        number = int(tokens[i+1])
        
        if operator == "+":
            answer += number
        elif operator == "-":
            answer -= number
            
    return answer