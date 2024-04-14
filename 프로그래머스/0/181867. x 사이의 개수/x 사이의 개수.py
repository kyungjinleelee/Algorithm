def solution(myString):
    answer = []
    # x를 기준으로 문자열 나누기 
    split_string = myString.split('x')
    
    # 각각의 길이로 배열 만들고 리턴
    for i in range(len(split_string)):
        answer.append(len(split_string[i]))
    return answer