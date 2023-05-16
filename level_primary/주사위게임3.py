from collections import Counter


def solution(a, b, c, d):
    answer = 0
    counter = Counter([a,b,c,d])
    case = len(counter)
    keys = list(counter.keys())
    values = list(counter.values())
    if case == 1:
        answer = keys[0]*1111
    elif case == 2:
        if values[0] == 2:
            answer = (keys[0] + keys[1]) * abs(keys[0] - keys[1])
        elif values[0] == 3:
            answer = (keys[0]*10 + keys[1]) ** 2
        else:
            answer = (keys[1]*10 + keys[0]) ** 2
    elif case == 3:
        ab = []
        for i,k in enumerate(values):
            if k == 1:
               ab.append(keys[i])
        answer = ab[0] * ab[1]
    else:
        answer = min(keys)

    return answer


print(solution(2,2,2,2 ))
print(solution(4,1,4,4 ))
print(solution(6,3,3,6 ))
print(solution(2,5,2,6 ))
print(solution(6,4,2,5 ))
