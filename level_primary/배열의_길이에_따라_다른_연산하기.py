def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for i,x in enumerate(arr):
            if i % 2 != 0:
                answer.append(n+x)
            else:
                answer.append(x)
    else:
        for i,x in enumerate(arr):
            if i % 2 != 0:
                answer.append(x)
            else:
                answer.append(n+x)
    return answer

print(solution([49, 12, 100, 276, 33],27))
print(solution([444, 555, 666, 777],100))