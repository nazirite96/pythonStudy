def solution(scoville, K):
    scoville.sort()
    maded_food_list = []
    answer = 0
    while len(scoville) >= 2:
        if len(maded_food_list) < 1 or maded_food_list[0] > scoville[0]:
            first = scoville.pop(0)
        else:
            first = made_food
        if first >= K:
            break
        if len(maded_food_list) < 1 or maded_food_list[0] > scoville[0]:
            second = scoville.pop(0)
        else:
            second = maded_food_list.pop(0)
        made_food = first + second * 2
        maded_food_list.append(made_food)
        answer += 1
    if scoville[0] < K:
        return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12],7))
# print(solution([1, 2, 3, 9, 10, 12],1000))