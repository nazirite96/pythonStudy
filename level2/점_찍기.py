import math


def solution(k, d):
    answer = 0

    for i in range(0,d+1,k):
        y = math.sqrt((d**2)-(i**2))
        answer += (y//k + 1)



    return int(answer)


print(solution(1,5))