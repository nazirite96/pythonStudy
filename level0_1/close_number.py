def solution(array, n):
    array.sort()
    answer = min(array, key=lambda x: abs( x - n))
    return answer

print(solution([12, 3, 4, 10, 13], 11))