def solution(array):
    answer = 0

    array.sort()
    answer = array[len(array)//2]
    print(array)
    return answer


array = [1, 2, 7, 10, 11]
print(solution(array))