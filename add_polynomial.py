def solution(polynomial):
    answer = ''
    num = 0
    added_poly = 0
    polynomial = polynomial.replace('+ ', '')
    poly = polynomial.split()
    for hang in poly:
        if hang.isdigit():
            num += int(hang)
        else:
            if len(hang) == 1:
                added_poly += 1
            else:
                hang = hang.replace('x', '')
                added_poly += int(hang)
    if added_poly == 1:
        answer = 'x'
    elif added_poly > 1:
        answer = str(added_poly)+'x'
    if len(answer) != 0 and num != 0:
        answer += ' + '+str(num)
    if len(answer) == 0:
        answer += str(num)

    return answer

print(solution("1 + 1 + 1"))