def solution(n, m, section):
    answer = 1

    next_pain_wall = section[0] + m - 1
    for sect in section:
        if next_pain_wall < sect:
            answer += 1
            next_pain_wall = sect + m - 1

    return answer

print(solution(8,4,[2,3,6]))