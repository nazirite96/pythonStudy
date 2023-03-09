def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    for i,a in enumerate(A):
        answer += a * B[i]
    return answer

print(solution([1, 4, 2],[5, 4, 4]))