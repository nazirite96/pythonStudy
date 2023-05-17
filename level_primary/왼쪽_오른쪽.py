def solution(str_list):
    answer = []

    for i,char in enumerate(str_list):
        if char == 'l':
            answer = str_list[:i]
            break
        elif char == 'r':
            answer = str_list[i+1:]
            break
    return answer


print(solution(str_list=["u", "u", "l", "r"]))