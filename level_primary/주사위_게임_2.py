def solution(a, b, c):
    case = len(set([a, b, c]))
    if case == 1:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    elif case == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        return a + b + c

print(solution(2,6,1))
print(solution(5,3,3))
print(solution(4,4,4))