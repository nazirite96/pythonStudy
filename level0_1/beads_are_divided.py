def solution(balls, share):
    answer = 0

    n = 1
    m = 1
    t = 1

    for i in range(1,balls+1):
        n *= i

    for i in range(1,share+1):
        m *= i

    for i in range(1,balls-share+1):
        t *= i

    print(n,',',m,',',t)

    answer = n / (t*m)

    return int(answer)


print(solution(5,3))