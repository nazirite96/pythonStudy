import itertools


def solution(expression):
    answer = 0
    expression = expression.replace('*',':*:').replace('+',':+:').replace('-',':-:')

    operrator = ['*', '-', '+']
    case_operrator_priority = list(itertools.permutations(operrator,3))
    for priority in case_operrator_priority:
        splited_list = expression.split(':')
        for operator in priority:
            # print(splited_list)
            while operator in splited_list:
                index = splited_list.index(operator)
                temp = 0
                if operator == '*':
                    temp = int(splited_list[index-1]) * int(splited_list[index + 1])
                elif operator == '+':
                    temp = int(splited_list[index-1]) + int(splited_list[index + 1])
                else:
                    temp = int(splited_list[index-1]) - int(splited_list[index + 1])
                del splited_list[index-1:index+2]
                splited_list.insert(index-1,temp)
        if answer < abs(splited_list[0]):
            answer = abs(splited_list[0])

    return answer

assert solution("100-200*300-500+20") == 60420