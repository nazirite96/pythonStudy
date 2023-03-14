def solution(n):
    answer = 0
    a = 0
    b = 1
    c = 0
    for i in range(2,n+1):
        answer = a + b
        a = b
        b = answer

    return answer % 1234567


print(solution(6))