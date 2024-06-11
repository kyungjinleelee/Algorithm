def solution(my_string):
    seen = set()
    result = []
    
    for str in my_string:
        if str not in seen:
            seen.add(str)
            result.append(str)
        
    return ''.join(result)