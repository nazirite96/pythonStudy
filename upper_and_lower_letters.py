def solution(my_string):
    answer = ''
    diff = ord('a')-ord('A')
    uni_list = [ord(str) for str in my_string]
    for i in range(len(uni_list)):
        if uni_list[i] >= 97:
            uni_list[i] = chr(uni_list[i] - diff)
        else:
            uni_list[i] = chr(uni_list[i] + diff)
    return answer.join(uni_list)

print(solution('hEllo'))