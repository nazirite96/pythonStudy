def solution(arr):
    answer = []
    arr_len = len(arr[0])
    n = len(bin(arr_len)[2:]) - 1
    print(n)
    for n_i in range(1, n):
        for y in range(0, arr_len, 2 * n_i):
            for x in range(0, arr_len, 2 * n_i):
                space = n_i * 2 - 1
                if arr[y][x] == arr[y + space][x + space] == \
                        arr[y + space][x] == arr[y][x + space]:
                    arr[y][x + space], arr[y + space][x], arr[y + space][x + space] = 3, 3, 3
    print(arr)
    zero_count = 0
    one_count = 0

    for line in arr:
        zero_count += line.count(0)
        one_count += line.count(1)

    answer.append(zero_count)
    answer.append(one_count)

    return answer


a = [[1, 1, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 1],
     [1, 1, 1, 1]]
b = [[1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 1, 1, 1, 1],
     [0, 1, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 1, 1, 1, 1]]
d = [[1, 1, 1, 3, 1, 3, 1, 3],
    [0, 1, 3, 3, 3, 3, 3, 3],
    [0, 0, 0, 3, 1, 3, 1, 3],
    [0, 1, 3, 3, 3, 3, 3, 3],
    [0, 3, 0, 3, 0, 3, 1, 1],
    [3, 3, 3, 3, 3, 3, 0, 1],
    [0, 3, 0, 3, 1, 0, 1, 3],
    [3, 3, 3, 3, 1, 1, 3, 3]]



c = [[1, 1],
     [1, 1]]

print(solution(b))
