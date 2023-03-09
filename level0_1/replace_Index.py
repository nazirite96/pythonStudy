def solution(my_string, num1, num2):
    answer = ''
    str_list = list(my_string)
    temp_str = str_list[num1]
    str_list[num1] = str_list[num2]
    str_list[num2] = temp_str
    return answer.join(str_list)

print(solution('hello', 1, 2))