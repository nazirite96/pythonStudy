def solution(arr):
    answer = []
    if 2 not in arr:
        return [-1]
    else:
        if arr.count(2) == 1:
            return [2]
        else:
            a = arr.index(2)
            b = 0
            for i in range(len(arr)-1, 0, -1):
                if arr[i] == 2:
                    b = i
                    break
            answer = arr[a:b+1]
    return answer

print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))