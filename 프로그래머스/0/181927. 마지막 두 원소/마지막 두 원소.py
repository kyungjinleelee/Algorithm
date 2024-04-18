def solution(num_list):
    a = num_list[-1]
    b = num_list[-2]
    if a > b:
        num_list.append(a - b)  
    else:
        num_list.append(a * 2)        
    return num_list

'''
주의할 것 
1. 무조건 for문 돌아야 한다고 생각하지 말 것 
2. 길거나 가독성을 해칠 만한 조건이 있으면 변수에 저장해서 쓸 것
'''