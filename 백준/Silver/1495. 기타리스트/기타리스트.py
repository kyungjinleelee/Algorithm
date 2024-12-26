n, s, m = map(int, input().split()) # n: 곡의 개수, s: 시작 볼륨, m: 최대 볼륨
v = list(map(int, input().split()))

def change_volume(n, s, m, v):
    # 현재 가능한 볼륨을 저장할 집합
    current_volumes = {s}

    for i in range(n):
        next_volumes = set()
        for vol in current_volumes:
            # 볼륨 더했을 때
            if 0 <= vol + v[i] <= m:
                next_volumes.add(vol + v[i])
            # 볼륨 뺐을 때
            if 0 <= vol - v[i] <= m:
                next_volumes.add(vol - v[i])

        # 다음 단계로 넘어갈 수 있는 볼륨 상태가 없으면 -1 출력
        if not next_volumes:
            return -1
        # 가능한 볼륨 상태 갱신
        current_volumes = next_volumes

    # 최종 가능한 볼륨 중 최대값 반환
    return max(current_volumes)

print(change_volume(n, s, m, v))