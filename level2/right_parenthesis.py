def solution(s):
    count = 0
    for s_paren in s:
        if s_paren == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    return count == 0