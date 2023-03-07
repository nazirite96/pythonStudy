def solution(k, score):
    answer = []
    rank = []
    for i in range(len(score)):
        rank.append(score.pop(0))
        rank.sort(reverse=True)
        if i <= k-1:
            answer.append(rank[i])
        else:
            answer.append(rank[k-1])
    return answer

print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))