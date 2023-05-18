def solution(n, m, section):
    answer = 0
    while len(section) != 0:
        start = section[0]
        end = start + m - 1
        while start <= section[0] <= end:
            section.pop(0)
            if len(section) == 0:
                break
        answer += 1
    return answer

print(solution(8, 4,[2,3,6]))
print(solution(5, 4,[1,3]))
print(solution(4, 1,[1, 2, 3, 4]))