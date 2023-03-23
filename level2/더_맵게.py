def solution(scoville, K):
    scoville.sort()
    answer = 0
    made_food = -1
    while scoville[0] < K:
        first = 0
        if made_food > scoville[0]:
            first = scoville.pop(0)
        else:
            first = made_food
        second = 0
        if made_food > scoville[0]:
            second = scoville.pop(0)
        else:
            second = made_food
        made_food = first + second * 2
        answer += 1

    if len(scoville) == 0:
        return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12],7))