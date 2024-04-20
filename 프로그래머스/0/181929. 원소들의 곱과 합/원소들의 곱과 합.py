def solution(num_list):
    product = 1
    # 모든 원소들의 합
    sum_of_squares = sum(num_list) * sum(num_list)
    
    # 모든 원소들의 곱
    for num in num_list:
        product *= num
        
    if product < sum_of_squares:
        return 1
    else:
        return 0