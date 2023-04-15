def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    while sum1 != sum2:
        if sum1 < sum2:
            poped = queue2.pop(0)
            queue1.append(poped)
            sum1 += poped
            sum2 -= poped
            answer += 1
        elif sum2 < sum1:
            poped = queue1.pop(0)
            queue2.append(poped)
            sum2 += poped
            sum1 -= poped
            answer += 1
        print(sum1, sum2)


    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

print(solution(queue1, queue2))

queue1 = [1, 1]
queue2 = [1, 5]

# print(solution(queue1, queue2))
