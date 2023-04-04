def solution(numbers):
    answer = []
    binary_num_list = [bin(num)[2:] for num in numbers]
    binary_answer = []
    for binary_num in binary_num_list:
        if '0' in binary_num:
            binary_answer.append(binary_num[:binary_num.rindex('0')] + '1' + binary_num[binary_num.rindex('0')+1:])
        else:
            binary_answer.append(('10'+binary_num[2:]))

    for bin_num in binary_answer:
        answer.append(int(bin_num,2))
    return answer

print(solution([5,7,8,9,10,11,12]))