import math

def solution(n):
    answer = 0
    least_one = n % 2
    two = 0
    while n >= least_one:
        answer += math.factorial(n+two) //( math.factorial(n) * math.factorial(two))
        n -= 2
        two += 1
    return answer

print(solution(2000))