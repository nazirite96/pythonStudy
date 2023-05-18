def solution(my_strings, parts):
    answer = ''
    for i, str in enumerate(my_strings):
        a, b = parts[i]
        answer += str[a:b+1]
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"],[[0, 4], [1, 2], [3, 5], [7, 7]] ))