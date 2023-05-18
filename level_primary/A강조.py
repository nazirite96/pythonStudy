def solution(myString):
    answer = ''
    str_list = list(myString)
    for i,str in enumerate(str_list):
        if str == 'a' or str == 'A':
            str_list[i] = 'A'
        else:
            str_list[i] = str.lower()
    return answer.join(str_list)


print(solution('abstract algebra'))
