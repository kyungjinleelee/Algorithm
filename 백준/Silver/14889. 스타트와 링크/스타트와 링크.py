from itertools import combinations

# 주어진 팀의 능력치를 계산
def calculate_team_score(team, stats):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += stats[team[i]][team[j]] + stats[team[j]][team[i]]
    return score

# 두 팀 간 능력치 차이의 최솟값 계산
def find_min_difference(n, stats):
    players = list(range(n))
    min_diff = float('inf')

    # 모든 가능한 팀 조합 탐색
    for start_team in combinations(players, n // 2):
        link_team = [player for player in players if player not in start_team]

        # 팀 능력치 계산
        start_score = calculate_team_score(start_team, stats)
        link_score = calculate_team_score(link_team, stats)

        # 능력치 차이 계산 및 최솟값 갱신
        min_diff = min(min_diff, abs(start_score - link_score))

    return min_diff

# 입력 받기
n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]

# 결과 계산 및 출력
result = find_min_difference(n, stats)
print(result)