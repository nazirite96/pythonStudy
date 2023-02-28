def solution(n):
    answer = 0
    for i in range(2, n+1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                answer += 1
    return answer

print(solution(10))