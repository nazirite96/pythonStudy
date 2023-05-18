def solution(arr, flag):
    answer = []
    for i,flag_ in enumerate(flag):
        if flag_:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop(-1)
    return answer


arr = [3, 2, 4, 1, 3]
flag = [True, False, True, False, False]

print(solution(arr, flag))
