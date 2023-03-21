def solution(n, k):
    answer = 0

    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    rev_base = '11111111111111111111111111111111111111111'
    print(rev_base)

    rev_base_splited = rev_base.split('0')

    for splited_str in rev_base_splited:
        if splited_str.isdigit():
            is_it_sosu = True
            num = int(splited_str)
            for i in range(2, int( num ** 1/2 ) + 1):
                if num % i == 0:
                    is_it_sosu = False
                    break
            if is_it_sosu and num != 1:
                answer += 1
    return answer

print(solution(1000000,2))

