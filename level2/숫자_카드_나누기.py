import math


def solution(arrayA, arrayB):
    answer = 0
    gcd = math.gcd(arrayA)
    a_yacso_list = [i for i in range(3,min(arrayA)+1,2)
                    if arrayA[0] % i == 0 and arrayA[1] % i == 0 ]
    b_yacso_list = [i for i in range(3,min(arrayB)+1,2)
                    if arrayB[0] % i == 0 and arrayB[1] % i == 0 ]
    if arrayA[0] % 2 == 0 and arrayA[1] % 2 == 0:
        a_yacso_list.append(2)
    if arrayB[0] % 2 == 0 and arrayB[1] % 2 == 0:
        b_yacso_list.append(2)
    for a_yacsoo in a_yacso_list:
        if arrayB[0] % a_yacsoo !=0 and arrayB[1] % a_yacsoo != 0:
            if answer < a_yacsoo:
                answer = a_yacsoo
    for b_yacsoo in b_yacso_list:
        if arrayA[0] % b_yacsoo !=0 and arrayA[1] % b_yacsoo != 0:
            if answer < b_yacsoo:
                answer = b_yacsoo
    return answer

a = [100000000,100000000]
b = [5, 20]

print(solution(a,b))

a = [10, 20]
b = [5, 17]

print(solution(a,b))

a = [14, 35, 119]
b = [18, 30, 102]
print(solution(a,b))