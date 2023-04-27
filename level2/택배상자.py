import collections


def solution(order):
    answer = 0
    sub_container_belt = collections.deque();
    i = 0

    for box in range(1,len(order)+1):
        if box == order[i]:
            answer += 1
            i += 1
            while sub_container_belt and order[i] == sub_container_belt[0]:
                sub_container_belt.popleft()
                i += 1
                answer += 1
        else:
            sub_container_belt.insert(0,box)

    return answer



order = [4, 3, 1, 2, 5]
print(solution(order))

order = [5, 4, 3, 2, 1]
print(solution(order))