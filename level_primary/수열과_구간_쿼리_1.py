def solution(arr, queries):
    for s,e in queries:
        for i in range(s,e+1):
            arr[i] += 1
    return arr

arr = [0, 1, 2, 3, 4]
queries = [[0, 1],[1, 2],[2, 3]]

print(solution(arr, queries))
