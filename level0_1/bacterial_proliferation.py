def solution(n, t):
    for i in range(t):
        n *= 2
    return n

print(solution(2,10))