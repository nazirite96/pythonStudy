def solution(n):
    answer = 0
    for y in range(n):
        for x in range(n):
            check_list = [[True for _ in range(n)] for _ in range(n)]
            answer += case_queen(x,y,check_list,0)
    return answer

def case_queen(x,y,check_list,count):
    pass

print(solution(4))