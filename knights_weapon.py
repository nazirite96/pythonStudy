def solution(number, limit, power):
    answer = 1
    for i in range(2,number+1):
        count = 2
        for j in range(2,int(i**(1/2))+1):
            if i % j == 0:
                count += 1
                if (j**2) != i :
                    count += 1
        if count > limit:
            answer += power
        else:
            answer += count
    return answer

print(solution(5, 3, 2))