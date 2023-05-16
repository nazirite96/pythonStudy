def solution(l, r):
    answer = []
    for k in range(1,128):
        s = int(bin(k)[2:])
        if l <= s*5 <= r:
            answer.append(s*5)
    if len(answer) == 0:
        return [-1]
    return answer

print(solution(5,555))