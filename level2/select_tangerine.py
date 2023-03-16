import collections


def solution(k, tangerine):
    answer = 0
    tangerine.sort(key= lambda tang : (tangerine.count(tang)))

    counter = collections.Counter(tangerine)
    tangerine_count = sorted(counter.values(),reverse=True)
    count = 0
    for count_t in tangerine_count:
        count += count_t
        answer += 1
        if count >= k:
            break
    return answer

print(solution(2,[5,5,5,5,5,5,5,5,5,5,8,1,1, 1, 1, 2, 2, 2, 3]))