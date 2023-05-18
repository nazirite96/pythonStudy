def solution(arr, queries):
    answer = []
    for i,j in queries:
        arr[j],arr[i] = arr[i],arr[j]
    answer = arr


    return answer

arr = [0,1,2,3,4]
queries = [[0, 3],[1, 2],[1, 4]]

print(solution(arr, queries))