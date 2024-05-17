def solution(my_string, overwrite_string, s):
    idx_zero = len(my_string) - (s + len(overwrite_string))
    
    if idx_zero != 0:
        return my_string[:s] + overwrite_string + my_string[-(idx_zero):]
    elif idx_zero == 0:
        return my_string[:s] + overwrite_string