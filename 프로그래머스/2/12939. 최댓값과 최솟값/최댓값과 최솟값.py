def solution(s):
    no_split = list(map(int, s.split()))
    min_str = min(no_split)
    max_str = max(no_split)
    return str(min_str) + " " + str(max_str)
