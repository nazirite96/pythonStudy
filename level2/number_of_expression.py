def solution(n):
    answer = 0
    list_sum_n = []
    natural_sum = 1
    index = 1
    while natural_sum <= n:
        list_sum_n.append(natural_sum)
        index += 1
        natural_sum += index
    for i, sum_num in enumerate(list_sum_n):
        x = n - sum_num
        x = x // (i+1)
        if n == (i+1) * x + sum_num:
            answer += 1
    return answer

print('result : ',solution(9))