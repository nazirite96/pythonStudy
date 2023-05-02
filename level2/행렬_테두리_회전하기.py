def solution(rows, columns, queries):
    answer = []

    number_map = [[(j - 1) * columns + i for i in range(1, columns + 1)] for j in range(1, rows + 1)]

    for query in queries:
        y1, x1, y2, x2 = (coord - 1 for coord in query)

        changed_numbers = []
        prev = number_map[y1 + 1][x1]

        for x in range(x1, x2 + 1):
            changed_numbers.append(number_map[y1][x])
            number_map[y1][x], prev = prev, changed_numbers[-1]

        for y in range(y1 + 1, y2 + 1):
            changed_numbers.append(number_map[y][x2])
            number_map[y][x2], prev = prev, changed_numbers[-1]

        for x in range(x2 - 1, x1 - 1, -1):
            changed_numbers.append(number_map[y2][x])
            number_map[y2][x], prev = prev, changed_numbers[-1]

        for y in range(y2 - 1, y1, -1):
            changed_numbers.append(number_map[y][x1])
            number_map[y][x1], prev = prev, changed_numbers[-1]

        answer.append(min(changed_numbers))

    return answer


rows = 6
columns = 6
queries =[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# queries =[[2,2,5,4]]
result = solution(rows, columns, queries)
print(result)
rows = 3
columns = 3
queries =[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
result = solution(rows, columns, queries)
print(result)
rows = 100
columns = 97
queries =[[1,1,100,97]]
result = solution(rows, columns, queries)
print(result)

[1,  2,   3,  4,  5,  6]
[ 7, 14,  8,  9, 11, 12]
[13, 20, 15, 10, 17, 18]
[19, 26, 21, 16, 23, 24]
[25, 27, 28, 22, 29, 30]
[31, 32, 33, 34, 35, 36]
