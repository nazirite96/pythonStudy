def solution(common):
    answer = 0

    a = common[1] - common[0]
    b = common[2] - common[1]
    if a==b:
        #등차 and 등비 1인 case
        answer = common[len(common)-1] + a
    else:
        #등비
        answer = common[len(common)-1] * (common[1] / common[0])

    return answer

common = [2, 4, 8]

print(solution(common))
