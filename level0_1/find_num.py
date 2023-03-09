def solution(num, k):
    answer = 0
    num_s = str(num)
    k_s = str(k)
    if k_s in num_s:
        answer = num_s.index(k_s)+1
    else:
        answer = -1
    return answer
