def solution(arr, k):
    answer = []
    is_full = False
    for s in arr:
        if s not in answer:
            answer.append(s)
        if len(answer) == k:
            break
            is_full = True
    if not is_full:
        while len(answer) != k:
            answer.append(-1)

    return answer


arr = [0, 1, 1, 1, 1]

print(solution(arr, 4))