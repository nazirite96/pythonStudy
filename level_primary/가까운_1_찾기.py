def solution(arr, idx):
    answer = -1

    for i in range(idx, len(arr)):
        if arr[i] == 1:
            answer = i

    return answer

print(solution([0, 0, 0, 1],1))