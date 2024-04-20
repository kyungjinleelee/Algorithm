def solution(num_list):
    odd_concat = ''
    even_concat = ''
    
    for num in num_list:
        if num % 2 != 0:
            odd_concat += str(num)
        else:
            even_concat += str(num)
    return int(odd_concat) + int(even_concat)