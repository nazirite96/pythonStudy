def solution(arr, query):
    for i,index in enumerate(query):
        if i % 2 == 0:
            arr = arr[0:index+1]
        else:
            arr = arr[index:]
    return arr

arr = [0, 1, 2, 3, 4, 5]
query = [4, 1, 2]

print(solution(arr, query))