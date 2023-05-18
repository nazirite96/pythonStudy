def solution(n):
    answer = []
    for i in range(n):
        line = []
        for j in range(n):
            if i == j:
                line.append(1)
            else:
                line.append(0)
        answer.append(line)
    return answer

print(solution(3))