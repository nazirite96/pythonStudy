import operator

def solution(k, tangerine):
    answer = 0
    set_tangerine = set(tangerine)

    tangerine_count = [tangerine.count(kg) for kg in set_tangerine]
    tangerine_count.sort(reverse=True)
    count = 0
    for count_t in tangerine_count:
        count += count_t
        answer += 1
        if count >= k:
            break
    return answer
    # dict_kg_count =  { kg:tangerine.count(kg) for kg in set_tangerine}
    # dict_kg_count = dict(sorted(dict_kg_count.items(), key=operator.itemgetter(1), reverse=True))
    # sum_count = 0
    # for kg in dict_kg_count.keys():
    #     sum_count += dict_kg_count.get(kg)
    #     answer += 1
    #     if sum_count >= k:
    #         break


print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))