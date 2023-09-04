answer = 0


def solution(n):
    global answer
    row = [True]*n
    r_dig = [True]*(2*n)
    l_dig = [True]*(2*n)

    def queen(r, remain):
        global answer
        if remain:
            for idx, i in enumerate(remain):
                if row[i] and r_dig[r-i] and l_dig[r+i]:
                    next_remain = remain[:idx] + remain[idx+1:]
                    row[i] = r_dig[r-i] = l_dig[r+i] = False
                    queen(r+1, next_remain)
                    row[i] = r_dig[r-i] = l_dig[r+i] = True
        else:
            answer += 1

    queen(0, list(range(n)))

    return answer


print(solution(4))
