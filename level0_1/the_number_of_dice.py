def solution(box, n):
    answer = 1
    for xyz in box:
        answer *= (xyz // n)
    return answer

print(solution([10, 8, 6], 3))