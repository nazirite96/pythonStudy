def solution(array):
    a = {}
    answer = 0

    for num in array:
        if a.__contains__(num):
            a[num] = a[num] + 1
        else:
            a[num] = 1
    max_value = max(a.values())
    arr_list = [k for k, v in a.items() if v == max_value]
    if len(arr_list) >= 2:
        answer = -1
    elif len(arr_list) == 1:
        answer = arr_list.pop()

    return answer


array = [1, 2, 3, 3, 3, 4, 4, 4]

print(solution(array))
