def solution(a, b):
    k = int(str(a)+str(b))
    if 2 * a * b > k:
        return 2 * a * b
    else:
        return k

print(solution(2,91))