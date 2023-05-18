def solution(arr1, arr2):
    answer = 0
    arr_one_len = len(arr1)
    arr_two_len = len(arr2)
    if arr_one_len == arr_two_len:
        arr_one_sum = sum(arr1)
        arr_two_sum = sum(arr2)
        if arr_two_sum > arr_one_sum:
            return -1
        elif arr_two_sum < arr_one_sum:
            return 1
        else:
            return 0
    elif arr_one_len > arr_two_len:
        return 1
    elif arr_one_len < arr_two_len:
        return -1

    return answer

print(solution([49, 13],[70, 11, 2]))
print(solution([100, 17, 84, 1],[55, 12, 65, 36]))
print(solution([1, 2, 3, 4, 5],	[3, 3, 3, 3, 3]))