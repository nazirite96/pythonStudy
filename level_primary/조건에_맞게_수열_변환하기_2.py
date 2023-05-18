def solution(arr):
    answer = 0
    before_arr = arr.copy()
    while True:
        for i, so in enumerate(arr):
            if 50 <= so and so % 2 == 0:
                arr[i] /= 2
            elif 50 > so and so % 2 == 1:
                arr[i] = arr[i] * 2 + 1
            print(answer , arr,before_arr)
        if before_arr == arr:
            break
        else:
            before_arr = arr.copy()
            answer += 1
    return answer

arr = [63, 2, 63, 51, 99, 99]

print(solution(arr))