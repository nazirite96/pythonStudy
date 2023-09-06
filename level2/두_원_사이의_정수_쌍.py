import math


def solution(r1, r2):
    answer = 0

    for y in range(0,r2+1):
        for x in range(1,r2+1):
            a = math.sqrt(((x*x) + (y*y)))
            if r2 >= a >= r1:
                answer += 1

    return answer * 4


print(solution(4,6))