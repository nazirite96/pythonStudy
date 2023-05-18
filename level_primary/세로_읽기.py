def solution(my_string, m, c):
    answer = my_string[c-1::m]
    return answer

str = "ihrhbakrfpndopljhygc"
m = 4
c = 2

print(solution(str,m,c))