def solution(n, m, section):
    answer = 0
    last_painted = 0  # 마지막으로 칠해진 구역의 끝
    
    for s in section:
        # 현재 구역이 마지막으로 칠한 구역보다 뒤에 있다면 새로운 칠이 필요
        if s > last_painted:
            answer += 1
            last_painted = s + m - 1  # 현재 구역에서 롤러의 범위 끝까지 칠함
    
    return answer
