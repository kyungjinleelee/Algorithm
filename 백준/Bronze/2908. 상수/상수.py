# 숫자 입력 받기
a, b = map(str, input().split()) # 734 893

# 상수의 방식으로 변환
a = a[::-1] # 437
b = b[::-1] # 398

# 두 개 중에 큰 수 출력
print(max(a, b))