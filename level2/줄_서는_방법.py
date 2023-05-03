import itertools
import math


def solution(n, k):
    answer = []

    n_list = [ i for i in range(1,n+1)]
    while 0 <= n - 1:
        n = n-1
        factorial = math.factorial(n)

        index = (k-1) // factorial
        answer.append(n_list.pop(index))
        k -= factorial*index


    return answer


print(solution(4,5))