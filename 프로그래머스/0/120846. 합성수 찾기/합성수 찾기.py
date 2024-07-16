def solution(n):
    def is_composite(num):
        count = 0
        # 1과 자신을 제외한 약수가 하나라도 있으면 합성수
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
            if count > 2:
                return True
        return False
    
    composite_cnt = 0
    for i in range(1, n + 1):
        if is_composite(i):
            composite_cnt += 1
    return composite_cnt