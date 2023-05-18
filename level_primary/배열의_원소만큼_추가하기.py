def solution(arr):
    answer = []
    for num in arr:
        for _ in range(num):
            answer.append(num)
    return answer

arr = [5, 1, 4]
print(solution(arr))