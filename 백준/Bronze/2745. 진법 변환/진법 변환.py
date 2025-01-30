N, B = input().split()
B = int(B) # B를 정수로 변환

# 10진법 변환 (파이썬 내장 함수 사용)
decimal_value = int(N, B)

print(decimal_value)