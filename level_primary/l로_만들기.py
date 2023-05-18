def solution(myString):
    answer = ''

    gijun = list('abcdefghijk')
    list_str = list(myString)
    for i,char in enumerate(list_str):
        if char in gijun:
            list_str[i] = 'l'
    return answer.join(list_str)

print(solution('abcdevwxyz'))
print(solution('jjnnllkkmm'))