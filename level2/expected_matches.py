def solution(n,a,b):
    answer = 1
    while a//2 != b//2:
        answer += 1
        a = a // 2 + 1
        b = b // 2 + 1
    return answer

print(solution(8,1,0))