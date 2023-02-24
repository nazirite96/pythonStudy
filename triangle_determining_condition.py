def solution(sides):
    answer = 0
    max = 0
    sum = 0
    for abc in sides:
        if max < abc:
            max = abc
        sum += abc
    sum -= max*2
    if sum > 0:
        answer = 1
    else:
        answer = 2

    return answer

print(solution([199, 72, 222]))