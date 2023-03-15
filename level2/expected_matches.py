def solution(n,a,b):
    answer = 0
    a = a-1
    b = b-1
    while True:
        answer += 1
        if a // 2 == b // 2:
            break
        a = a // 2
        b = b // 2
    return answer

print(solution(2 ** 20,1,2 ** 20))
print(solution(8,4,8))