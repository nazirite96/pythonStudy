def solution(n, numlist):
    answer = [num for num in numlist if num % 3 == 0]
    return answer


print(solution(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))