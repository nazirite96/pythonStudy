def solution(arr):
    stk = []

    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[len(stk)-1] < arr[i]:
                stk.append(arr[i])
                i+=1
            else:
                stk.pop(len(stk)-1)
    return stk

arr = [1, 4, 2, 5, 3]
print(solution(arr))