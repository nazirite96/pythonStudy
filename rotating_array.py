def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers.pop(len(numbers)-1))
    else:
        numbers.append(numbers.pop(0))

    return numbers


print(solution([455, 6, 4, -1, 45, 6, 4], 'left'))