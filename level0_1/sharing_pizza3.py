def solution(slice, n):
    answer = 0
    at_least_pizza_silce = 0;
    while at_least_pizza_silce <= n:
        at_least_pizza_silce += slice
        if at_least_pizza_silce != n:
            answer +=1

    return answer


print(solution(2,1))