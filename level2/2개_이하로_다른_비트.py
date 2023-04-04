def solution(numbers):
    answer = []
    binary_num_list = [bin(num)[2:] for num in numbers]

    for binary_num in binary_num_list:
        if '0' in binary_num:
            binary_num[:binary_num.rindex('0')]+'1'+''
        else:
            pass


    return answer

print(solution([5,7,8,9,10,11,12]))