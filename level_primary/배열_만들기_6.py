def solution(arr):
    answer = []
    i = 0
    for k in arr:
        if len(answer) == 0:
            i = 0
            answer.append(k)
        else:
            if answer[i] == k:
                answer.pop(i)
                i -= 1
            else:
                answer.append(k)
                i += 1
    if len(answer) == 0:
        return [-1]
    return answer

arr = [0, 1, 1, 1, 0]
print(solution(arr))
arr = [0, 1, 0, 1, 0]
print(solution(arr))
arr = [0, 1, 1, 0]
print(solution(arr))