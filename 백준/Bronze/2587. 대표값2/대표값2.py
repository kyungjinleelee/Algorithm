numbers = [int(input()) for _ in range(5)]

mean = sum(numbers) // 5  # 평균
median = sorted(numbers)[2]  # 중앙값

print(mean)
print(median)