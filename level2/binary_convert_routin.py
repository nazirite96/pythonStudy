def solution(s):
    a = 0
    b = 0
    while s != '1':
        a += 1
        b += s.count('0')
        s = s.replace('0','')
        print(s)
        s = bin(len(s))[2:]
    return [a, b]

print(solution("01110"))