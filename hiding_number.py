import re

def solution(my_string):
    answer = 0
    my_string = re.sub('[a-zA-Z]',' ',my_string)
    str_list = my_string.split(' ')
    for str_num in str_list:
        if str_num.isdigit():
            answer += int(str_num)
    return answer

print(solution("aAb1B2cC34oOp"))