def solution(my_string, is_suffix):
    suffix_list = [my_string[i:] for i in range(len(my_string))]
    return int(is_suffix in suffix_list)

print(solution('banana','ana'))
print(solution('banana','nan'))