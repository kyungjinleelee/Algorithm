N, B = map(int, input().split())

result = ""
# 10진수를 B진법으로 변환
while N > 0:
    remainder = N % B # 나머지 계산
    if remainder < 10:
        result += str(remainder) # 0~9는 그대로 사용
    else:
        result += chr(remainder - 10 + ord('A')) # # 10~35는 A~Z 변환
    N //= B # 몫 업데이트

print(result[::-1])