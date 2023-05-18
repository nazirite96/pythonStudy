def solution(my_string, indices):
    answer = ''
    my_string_list = list(my_string)
    for index in indices:
        my_string_list[index] = ''
    print(my_string_list)
    return answer.join(my_string_list)

my_string = 'apporoograpemmemprs'
indices = [1, 16, 6, 15, 0, 10, 11, 3]

print(solution(my_string, indices))
