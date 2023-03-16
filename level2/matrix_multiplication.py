def solution(arr1, arr2):
    coulnm = []
    for i,a in enumerate(arr1):
        row = []
        for b in range(len(arr2[0])):
            sum = 0
            for j,a_num in enumerate(a):
                sum += a_num * arr2[j][b]
            row.append(sum)
        coulnm.append(row)
    return coulnm

print(solution([[1, 2], [3, 4]],
               [[5, 6, 7], [8,9,10]]))