import math
def solution(clothes):
    answer = 0
    dict_type_of_cloth = {}
    for cloth in clothes:
        if cloth[1] in dict_type_of_cloth:
            dict_type_of_cloth[cloth[1]].append(cloth[0])
        else:
            dict_type_of_cloth[cloth[1]] = [cloth[0]]
    # 조합식
    answer = 1
    for type in dict_type_of_cloth.keys():
        cloth_count = len(dict_type_of_cloth.get(type))
        answer *= math.factorial(cloth_count) // math.factorial(cloth_count-1) + 1
    answer -= 1

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
