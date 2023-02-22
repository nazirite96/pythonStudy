def solution(n):
    answer = 0
    n2 = n;
    while n2 % 6 != 0:
        n2 += n

    answer = n2 // 6

    return answer

print(solution(4))