def solution(arr):
    a = 1
    arr_len = len(arr)
    while arr_len > a:
        a *= 2
    for _ in range(arr_len, a):
        arr.append(0)
    return arr

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([58, 172, 746, 89]))