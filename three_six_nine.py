def solution(order):
    answer = 0
    order_s = str(order)
    for o in order_s:
        if o == '3' or o =='6' or o == '9':
            answer += 1
    return answer

print(solution(29423))