def solution(s):
    answer = 0
    s_list = list(s)
    dict_parenthesis = { '}':'{',
                         ']':'[',
                         ')':'('}
    for i in range(len(s)):
        parenthesis_check_list = []
        index = 0
        for s_char in s_list:
            if index == 0 or parenthesis_check_list[index-1] != dict_parenthesis.get(s_char):
                parenthesis_check_list.append(s_char)
                index += 1
            else:
                parenthesis_check_list.pop(index-1)
                index -= 1
        if len(parenthesis_check_list) == 0:
            answer += 1
        s_list.append(s_list.pop(0))
    return answer


print(solution("[)(]"))