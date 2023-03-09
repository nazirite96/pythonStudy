def solution(numer1, denom1, numer2, denom2):
    answer_numer = denom1 * numer2 + numer1 * denom2
    answer_denom = denom1 * denom2

    for i in range(answer_denom,1,-1):
        if answer_denom % i == 0:
            if answer_numer % i == 0:
                answer_denom /= i
                answer_numer /= i

    answer = [int(answer_numer), int(answer_denom)]

    return answer


print(solution(999,999,999,999))