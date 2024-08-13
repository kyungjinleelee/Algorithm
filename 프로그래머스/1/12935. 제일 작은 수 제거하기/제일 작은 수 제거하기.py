def solution(arr):
    # 예외 처리
    if len(arr) == 1:
        return [-1]
    
    # 가장 작은 수 찾아서 제거
    min_value = min(arr)
    arr.remove(min_value)
    return arr