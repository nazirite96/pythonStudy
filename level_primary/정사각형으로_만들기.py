def solution(arr):
    answer = [[]]
    height = len(arr)
    width = len(arr[0])

    if height == width:
        return arr
    elif height > width:
        k = height - width
        for line in arr:
            for _ in range(k):
                line.append(0)
    elif width > height:
        k = width - height
        line = [ 0 for _ in range(width)]
        for _ in range(k):
            arr.append(line)


    return arr

print(solution([[1, 2], [3, 4]]))