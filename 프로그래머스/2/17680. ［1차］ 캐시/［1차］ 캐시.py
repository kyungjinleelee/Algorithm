def solution(cacheSize, cities):
    run_time = 0
    cache = []
    
    # 예외 처리
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        
        # 캐시 미스면
        if city not in cache:
            # 캐시가 가득 안찼으면 추가하고 실행시간 5 추가
            if len(cache) < cacheSize:
                cache.append(city)
            # 캐시 가득찼으면 LRU로 교체하셈
            else:
                cache.pop(0)
                cache.append(city)
            run_time += 5
        # 캐시 히트면     
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            run_time += 1
    return run_time