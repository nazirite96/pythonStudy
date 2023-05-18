def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        t = int(num[s:s+l])
        if t > k:
            answer.append(t)
    return answer

print(solution(["0123456789","9876543210","9999999999999"],50000,5,5))