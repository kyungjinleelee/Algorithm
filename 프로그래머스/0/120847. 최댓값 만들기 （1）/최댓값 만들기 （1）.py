import itertools 

def solution(numbers):
    combinations = itertools.combinations(numbers, 2)
    max_product = 0
    
    for combo in combinations:
        num1, num2 = combo
        product = num1 * num2
        # 최대값 갱신
        max_product = max(max_product, product)
    return max_product