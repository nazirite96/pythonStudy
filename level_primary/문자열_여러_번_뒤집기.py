def solution(my_string, queries):
    answer = ''
    str_list = list(my_string)
    for a,b in queries:
        reverse_str = str_list[a:b + 1]
        reverse_str.reverse()
        for i in range(a,b+1):
            str_list[i] = reverse_str.pop(0)
            char = 'a'
            if char.islower():
                char.upper()
    return answer.join(str_list)
my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

print(solution(my_string,queries))