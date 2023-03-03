def solution(numlist, n):
    answer = []
    right = 0
    left = 0

    numlist.append(n)
    numlist.sort()

    numlist_right = numlist[numlist.index(n)+1:]
    numlist_left = numlist[:numlist.index(n)]
    print(numlist_left)
    print(numlist_right)
    while len(numlist_right) != 0:
        if right == 0:
            right = numlist_right.pop(0)
        if len(numlist_left) != 0 and left == 0:
            left = numlist_left.pop()
        if abs(right-n) <= abs(left-n) or left == 0:
            answer.append(right)
            right = 0
        else:
            answer.append(left)
            left = 0
    if right != 0:
        answer.append(right)
    while len(numlist_left) != 0:
        answer.append(numlist_left.pop())
    return answer

print(solution([1, 2, 3, 4, 5, 6], 4))