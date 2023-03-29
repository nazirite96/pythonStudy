def solution(dirs):
    answer = 0
    x = 0
    y = 0
    visited_point = {}
    for command in dirs:
        before = str(x) + str(y)
        if command == 'L' and x > -5:
            x -= 1
        if command == 'R' and x < 5:
            x += 1
        if command == 'U' and y < 5:
            y += 1
        if command == 'D' and y > -5:
            y -= 1
        after = str(x) + str(y)

        if before != after:
            if before not in visited_point:
                if after not in visited_point:
                    visited_point[before] = [after]
                elif before not in visited_point[after]:
                    visited_point[before] = [after]
            elif after not in visited_point[before]:
                if after not in visited_point or before not in visited_point[after]:
                    visited_point[before].append(after)
    for point in visited_point.keys():
        answer += len(visited_point[point])

    return answer

print(solution("LLLLLRRRRRUUUUUDDDDD"))