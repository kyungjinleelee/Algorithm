def solution(a, b):
    str_ver = int(str(a) + str(b))
    product_ver = 2 * a * b
    
    return max(str_ver, product_ver)