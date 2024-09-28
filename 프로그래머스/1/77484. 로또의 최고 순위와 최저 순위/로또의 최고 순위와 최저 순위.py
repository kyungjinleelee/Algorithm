def solution(lottos, win_nums):
    '''
    최고 순위: 0이 모두 당첨 번호에 해당한다고 가정하고, 맞춘 숫자의 개수에 0의 개수를 더하여 계산
    최저 순위: 0을 모두 제외하고, lottos와 win_nums에서 겹치는 숫자를 세서 계산
    ''' 
    
    # 0의 개수와 맞춘 번호의 갯수 세기
    zeros = lottos.count(0)
    correct = len(set(lottos) & set(win_nums))

    # 최고 순위: 0을 모두 맞췄다고 가정 (현재 맞춘 개수 + 0의 개수)
    max_rank = min(7 - (correct + zeros), 6)  # 최고 순위
    # 최저 순위: 0이 모두 틀렸다고 가정 (현재 맞춘 개수)
    min_rank = min(7 - correct, 6)  # 최저 순위
    
    return [max_rank, min_rank]