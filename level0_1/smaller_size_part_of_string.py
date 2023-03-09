def solution(t, p):
    answer = 0
    p_num = int(p)
    p_len = len(p)
    for i in range(len(t)-(p_len-1)):
        if int(t[i:i+p_len]) <= p_num:
            answer+=1

    return answer

print(solution('3141592','271'))