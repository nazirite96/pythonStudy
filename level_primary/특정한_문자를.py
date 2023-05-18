def solution(my_string, alp):
    answer = ''
    list_str = list(my_string)
    for i,char in enumerate(list_str):
        if char == alp:
            list_str[i] = char.upper()
    return answer.join(list_str)