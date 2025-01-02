n = int(input())
scores = list(map(int, input().split()))

m = max(scores)
new_scores = []
for score in scores:
    score = score / m * 100
    new_scores.append(score)

new_average = sum(new_scores) / len(new_scores)
print(new_average)