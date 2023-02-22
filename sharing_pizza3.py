def solution(slice, n):
    answer = 1
    at_least_pizza_silce = slice;
    while at_least_pizza_silce <= n:
        at_least_pizza_silce += slice
        answer +=1

    return answer


print(solution(4,12))