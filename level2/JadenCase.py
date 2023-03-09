def solution(s):
    answer = ''
    s = s.lower()
    s = list(s)
    for i,s_char in enumerate(s):
        if i == 0:
            s[i] = s[i].upper()
        if i == len(s)-1:
            break
        if s_char == ' ':
            s[i+1] = s[i+1].upper()
    return answer.join(s)

print(solution("3people unFollowed me"))