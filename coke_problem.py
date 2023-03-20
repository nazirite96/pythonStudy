def solution(a, b, n):
    answer = 0
    diff = a - b
    while n // a != 0:
        n -= diff
        answer += b
    return answer

print(solution(5, 3, 21))