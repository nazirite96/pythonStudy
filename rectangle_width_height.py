def solution(dots):
    answer = 0
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    return abs(max(x)-min(x)) * abs(max(y)-min(y))

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))