def solution(s):
    answer = 0
    k = ''
    k_count = 0
    no_k_count = 0
    for s_char in s:
        is_not_done = True
        if k_count == 0:
            k = s_char
        if s_char == k:
            k_count += 1
        else:
            no_k_count += 1

        if k_count == no_k_count:
            is_not_done = False
            k_count = 0
            no_k_count = 0
            answer += 1
    if is_not_done:
        answer += 1
    return answer

print(solution('abracadabra'))