def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    if a != b and a < b:
        return -1
    elif a != b and a > b:
        return 1
    elif a == b:
        return check(arr1, arr2)
    
def check(arr1, arr2):
    total = 0
    total2 = 0
    # 각 배열의 모든 원소의 합 비교
    for num in arr1:
        total += num
    for num in arr2:
        total2 += num
    
    # 다르다면 더 큰 쪽이 큼
    if total > total2:
        return 1
    elif total < total2:
        return -1
    # 같다면 같음
    else:
        return 0      
    