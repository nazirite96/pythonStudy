def solution(n):
    answer = []
    x, x_min, x_max = 0, 0, n
    y, y_min, y_max = 0, 0, n
    start = 1
    end = n ** 2
    for i in range(n):
        list = []
        for j in range(n):
            list.append(0)
        answer.append(list)
    while start <= end:
        # right
        for _x in range(x_min,x_max):
            answer[y][_x] = start
            start += 1
            x = _x
        y_min += 1
        # down
        for _y in range(y_min,y_max):
            answer[_y][x] = start
            start += 1
            y = _y
        x_max -= 1
        # left
        for _x in range(x_max-1,x_min-1,-1):
            answer[y][_x] = start
            start += 1
            x = _x
        # up
        y_max -= 1
        for _y in range(y_max-1,y_min-1,-1):
            answer[_y][x] = start
            start += 1
            y = _y
        x_min += 1
        print(answer)


    return answer

[[1, 2, 3, 4],
 [12, 13, 14, 5],
 [11, 16, 15, 6],
 [10, 9, 8, 7]]
[[1, 2, 3, 4, 5],
 [16, 17, 18, 19, 6],
 [15, 24, 0, 20, 7],
 [14, 23, 22, 21, 8],
 [13, 12, 11, 10, 9]]

[[1, 2, 3, 4, 5, 6, 7],
 [24, 25, 26, 27, 28, 29, 8],
 [23, 40, 41, 42, 43, 30, 9],
 [22, 39, 48, 49, 44, 31, 10],
 [21, 38, 47, 46, 45, 32, 11],
 [20, 37, 36, 35, 34, 33, 12],
 [19, 18, 17, 16, 15, 14, 13]]

print(solution(7))