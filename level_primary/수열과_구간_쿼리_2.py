def solution(arr, queries):
    answer = []

    for query in queries:
        s = 1000001
        for i in range(query[0],query[1]+1):
            if s > arr[i] > query[2]:
                s = arr[i]
        if s == 1000001:
            answer.append(-1)
        else:
            answer.append(s)
    return answer

arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

print(solution(arr, queries))

