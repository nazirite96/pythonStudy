def solution(s):
    answer = ' '
    number_list = [int(str) for str in s.split()]
    print(number_list)
    return str(min(number_list))+answer+str(max(number_list))

print(solution("-1 -2 -3 -4"))