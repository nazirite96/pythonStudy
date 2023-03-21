def solution(numbers, target):
    answer = []
    is_it_to_be_target(0, len(numbers), numbers, target, '', 0,answer)

    return len(answer)

def is_it_to_be_target(dept, until, numbers, target, operator_char, sum, answer):
    if dept == 0:
        is_it_to_be_target(1,until,numbers,target,'+',sum,answer)
        is_it_to_be_target(1,until,numbers,target,'-',sum,answer)
    else:
        dept += 1
        numbers_copy = numbers.copy()
        num = numbers_copy.pop(0)
        if operator_char == '+':
            sum += num
            if dept == until+1:
                if sum == target:
                    answer.append(1)
                return
            is_it_to_be_target(dept,until, numbers_copy, target, '+', sum,answer)
            is_it_to_be_target(dept,until, numbers_copy, target, '-', sum,answer)
        else:
            sum -= num
            if dept == until+1:
                if sum == target:
                    answer.append(1)
                return
            is_it_to_be_target(dept,until, numbers_copy, target, '+', sum,answer)
            is_it_to_be_target(dept,until, numbers_copy, target, '-', sum,answer)



print(solution([1, 1, 1, 1, 1], 3))
