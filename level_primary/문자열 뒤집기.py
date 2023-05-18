def solution(my_string, s, e):
    answer = my_string[:s] + my_string[s:e + 1][::-1] + my_string[e+1:]
    return answer

my_str = 'Progra21Sremm3'
s = 6
e = 12

print(solution(my_str, s, e))