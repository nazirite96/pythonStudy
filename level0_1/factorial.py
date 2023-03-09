def solution(n):
    answer = 1
    fac = 1
    for i in range(1, 10+1):
        fac *= i
        print(fac,i)
        if fac == n:
            answer = i
            break
        if fac > n:
            answer = i-1
            break
    return answer

print(solution(7))

