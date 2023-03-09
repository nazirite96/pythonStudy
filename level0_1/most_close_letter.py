def solution(s):
    answer = []
    s_list = []
    for i,s_letter in enumerate(s):
        if s_letter in s_list:
            answer.append(i-s_list.index(s_letter))
            s_list[s_list.index(s_letter)] = 'checked'
        else:
            answer.append(-1)
        s_list.append(s_letter)

    return answer

print(solution('banana'))