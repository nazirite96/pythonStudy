import math


def solution(arrayA, arrayB):
    answer = 0
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    for a in arrayA:
        gcd_a = math.gcd(gcd_a,a)
    for b in arrayB:
        gcd_b = math.gcd(gcd_b,b)
    cant_div_a_to_b = True
    cant_div_b_to_a = True
    for a in arrayA:
        if a % gcd_b == 0 or gcd_b == 1:
            cant_div_a_to_b = False
            break
    for b in arrayB:
        if b % gcd_a == 0 or gcd_a == 1:
            cant_div_b_to_a = False
            break
    if cant_div_b_to_a and cant_div_a_to_b:
        return max(gcd_b,gcd_a)
    elif cant_div_a_to_b:
        return gcd_b
    elif cant_div_b_to_a:
        return gcd_a

    return answer

a = [100000000,100000000]
b = [5, 20]

a = [10, 17]
b = [5, 20]

print(solution(a,b))

a = [10, 20]
b = [5, 17]

print(solution(a,b))

a = [14, 35, 119]
b = [18, 30, 102]
print(solution(a,b))

a = [14, 35, 119]
b = [18, 30, 102]
print(solution(a,b))

a = [5]
b = [8]
print(solution(a,b))

a = [10, 20]
b = [5, 17, 20]
print(solution(a,b))