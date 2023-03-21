def solution(n,left,right):
    answer = []
    for i in range(n):
        if left//n > i:
            pass
        elif i > right//n:
            break
        else:
            for j in range(n):
                num = 0
                if j > i:
                    num = j + 1
                else:
                    num = j + 1 + (i - j)
                answer.append(num)
    right  = right - left +1
    return answer[left % n:left % n + right]

print(solution(3,2,5))