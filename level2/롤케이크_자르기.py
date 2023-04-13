from collections import Counter

def solution(topping):
    answer = 0
    a = dict(Counter(topping))
    b = set()

    for topp in topping:
        a[topp] -= 1
        if a[topp] == 0:
            del a[topp]
        b.add(topp)
        if len(a) == len(b):
            answer += 1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# print(solution([1, 2, 3, 1, 4]))
