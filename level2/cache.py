def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        print(cache)
        if city in cache:
            answer += 1
            cache.append(city)
            cache.pop(cache.index(city))
        else:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
    return answer

print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))