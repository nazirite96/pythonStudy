def solution(str1, str2):
    answer = ''
    a = list(str1)
    b = list(str2)
    for _ in range(len(str1) * 2):
        if _ % 2 == 0:
            answer += a.pop(0)
        else:
            answer += b.pop(0)
    return answer

print(solution('aaaa','bbbb'))