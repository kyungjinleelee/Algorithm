def solution(s):
    # 가운데 인덱스 계산
    mid = len(s) // 2
    
    if len(s) % 2 != 0:
        return s[mid]
    else:
        return s[mid-1:mid+1]