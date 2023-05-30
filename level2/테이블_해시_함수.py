def solution(data, col, row_begin, row_end):
    answer = 0
    row_end -= 1
    row_begin -= 1
    moded_datas = []
    sorted_data = sorted(data, key=lambda x: (x[col-1],  -x[0]))
    for i, line in enumerate(sorted_data):
        if row_begin <= i <= row_end:
            moded_data = 0
            for value in line:
                moded_data += value % (i + 1)
            moded_datas.append(moded_data)
    for value in moded_datas:
        answer ^= value

    return answer


data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3

print(solution(data, col, row_begin, row_end))

