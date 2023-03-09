def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(m-1,len(score),m):
        answer+=(score[i] * m)
    return answer

print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))