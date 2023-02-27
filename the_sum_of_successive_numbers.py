def solution(num, total):
    answer = []
    sum_num = 0
    base_num = 0
    for i in range(1,num+1):
        sum_num+=i
    base_num = int((total - sum_num) / num)
    for i in range(1,num+1):
        answer.append(base_num+i)

    return answer

print(solution(3,12))