import sys
N = sys.stdin.readline().strip()

result = 0

# 1의 자리일 때는 그냥 바로 출력하기
if len(N) == 1:
    result = int(N)
# 1의 자리가 아니면 11부터 시작
else:
    result = 11
    for i in range(2, 10): # N이 최대 1억이니 9까지만 탐색
        # N의 자리수를 찾으면, 그 숫자의 자리수 *(그 숫자의 자리수-1에 해당하는 숫자 영역)을 해서 더해줌
        if len(N) == i:
            result += i * (int(N) - (10 ** (i - 1)))
            break
        # 자리수가 다르면, 자리수에 해당하는 최대 갯수만큼 누적해서 더하기
        else:
            result += i * (9 * 10 ** (i - 1)) + 1

print(result)