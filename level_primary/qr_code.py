def solution(q, r, code):
    answer = ''
    for index,char in enumerate(code):
        if index % q == r:
            answer += char
    return answer


print(solution(3,1,'qjnwezgrpirldywt'))