def solution(weights):
    visit = [-1 for _ in range(4001)]
    Same = [-1 for _ in range(1001)]

    cnt = 0
    for i in range(len(weights)):
        Same[weights[i]] += 1
        cnt += Same[weights[i]]
        SameCnt = Same[weights[i]]

        for j in range(2, 5):
            visit[weights[i] * j] += 1
            cnt += (visit[weights[i] * j] - SameCnt)

    return cnt

weights = [100, 100, 300, 100, 600]

print(solution(weights))