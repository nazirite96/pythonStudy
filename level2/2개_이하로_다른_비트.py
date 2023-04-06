def solution(numbers):
    answer = []
    print(numbers[0])
    binary_num_list = [bin(num)[2:] for num in numbers]
    binary_answer = []
    for binary_num in binary_num_list:
        print(binary_num)
        if binary_num[-1] == '0':
            binary_answer.append(binary_num[:-1] + '1')
        else:
            if '0' in binary_num:
                binary_answer.append(binary_num[:binary_num.rindex('0')] + '10' + binary_num[binary_num.rindex('0')+2:])
            else:
                binary_answer.append(('10'+binary_num[1:]))

    for bin_num in binary_answer:
        print(bin_num)
        answer.append(int(bin_num,2))
    return answer

print(solution([10**15]))