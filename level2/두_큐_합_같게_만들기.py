def solution(queue1, queue2):
    answer = 0
    start = 0
    end = len(queue1)
    now = sum(queue1)
    l = queue1 + queue2
    goal = sum(l) / 2
    while goal != now :
        if goal > now:
            if len(l) == end:
                return -1
            now += l[end]
            end += 1
            answer += 1
        else:
            now -= l[start]
            start += 1
            answer += 1

    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

print(solution(queue1, queue2))

queue1 = [1, 1]
queue2 = [1, 5]

print(solution(queue1, queue2))


queue1 = [1,2,9,4]
queue2 = [1,1,2,2]

print(solution(queue1, queue2))