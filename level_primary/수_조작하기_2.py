def solution(numLog):
    answer = ''

    for i in range(1,len(numLog)):
        cha = numLog[i]-numLog[i-1]
        if cha == 10:
            answer += 'd'
        elif cha == -10:
            answer += 'a'
        elif cha == 1:
            answer += 'w'
        else:
            answer.sp
            answer += 's'

    return answer

log =[0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]

print(solution(log))