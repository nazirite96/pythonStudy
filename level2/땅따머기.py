def solution(land):
    answer = 0
    line_1 = land.pop(0)
    max_in_line = max(line_1)
    answer += max_in_line
    exclude_next_index = line_1.index(max_in_line)
    for line in land:
        line[exclude_next_index] = -1
        print(line)
        max_in_line = max(line)
        answer += max_in_line
        exclude_next_index = line.index(max_in_line)

    return answer

print(solution([[100,1,1,1],[100,2,1,1],[100,1,3,1],[100,1,4,1],[100,1,4,1],[100,1,4,1],[100,1,4,1],[100,1,4,1]]))