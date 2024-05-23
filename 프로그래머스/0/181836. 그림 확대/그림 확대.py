def solution(picture, k):
    answer = []
    
    for pic in picture:
        enlarge_pic = ''
        # 각 문자를 k번 반복하기
        for p in pic:
            enlarge_pic += p * k
        # 확장된 행을 k번 반복하기
        for _ in range(k):
            answer.append(enlarge_pic)
    return answer