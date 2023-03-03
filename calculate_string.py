def solution(my_string):
    answer = 0
    splited_str = my_string.split()
    num = []
    opperators = []
    for str in splited_str:
        if str.isdigit():
            num.append(int(str))
        else:
            opperators.append(str)
    answer = num.pop(0)

    for i,opperator in enumerate(opperators):
        if opperator == '+':
            answer += num[i]
        else:
            answer -= num[i]
    return answer

print(solution("3 + 4"))