def solution(numbers, n):
    answer = 0

    for num in numbers:
        answer += num
        if answer > n:
            break

    return answer

print(solution([34, 5, 71, 29, 100, 34],123))