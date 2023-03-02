def solution(n):
    if n == 1:
        return [1]
    answer = [1, n]
    for i in range(2,int(n/2+1)):
        if n % i == 0:
            print(i)
            answer.append(i)
    answer.sort()
    return answer


print(solution(1))