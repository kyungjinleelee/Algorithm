words = [input().strip() for _ in range(5)]

result = ""
for col in range(15): # 최대 15열까지 순회
    for row in range(5):
        # 해당 row에서 유효한 col인지 확인
        if col < len(words[row]):
            result += words[row][col]

print(result)