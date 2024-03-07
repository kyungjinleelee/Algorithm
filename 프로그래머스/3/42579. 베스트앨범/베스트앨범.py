def solution(genres, plays):
    answer = []
    playDic = {}      # {장르: 총 재생 횟수}
    dic = {}        # {장르: [(플레이 횟수, 고유번호)]}
    
    # 해시 만들기
    for i in range(len(genres)):
        playDic[genres[i]] = playDic.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i], i)]
        
    # 재생 횟수 내림차순으로 장르 별 정렬
    genreSort = sorted(playDic.items(), key = lambda x: x[1], reverse = True)
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르 별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        dic[genre] = sorted(dic[genre], key = lambda x: (-x[0], x[1]))
        
        answer += [idx for (play, idx) in dic[genre][:2]]
    return answer