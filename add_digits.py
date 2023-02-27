def solution(n):
    answer = 0
    list_n = list(str(n))
    for num_s in list_n:
        answer+= int(num_s)
    return answer

print(solution(1234))